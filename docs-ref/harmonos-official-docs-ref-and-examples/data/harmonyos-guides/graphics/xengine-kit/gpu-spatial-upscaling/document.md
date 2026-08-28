# GPU Spatial Upscaling

XEngine Kit provides the GPU spatial upscaling capability. Based on input images of a single frame, it uses spatial neighborhood information for super-sampling, offering low overhead with significant benefits. The recommended upscaling factor is \[1.2, 1.5\].

#### Restrictions

-   Phones are supported. Additionally, tablets and PCs/2-in-1 devices are supported since version 5.0.2(14), and TVs are supported since version 5.1.0(18).
-   You can check whether an extension is supported as follows:
    
    \- For OpenGL ES, use the extension query API [HMS\_XEG\_GetString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_getstring).
    
    \- For Vulkan, use the extension query API [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties).
    
    If the query result contains [XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#xeg_spatial_upscale_extension_name), the extension is supported; otherwise, the extension is not supported.
    

#### API Description

The following lists OpenGL ES and Vulkan APIs used for GPU spatial upscaling setting. For details about more setting and query APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine).

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

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_SpatialUpscaleParameter (GLenum pname, GLvoid \*param)

 | 

Sets the input parameters for GPU spatial upscaling.

 |
| 

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_RenderSpatialUpscale (GLuint inputTexture)

 | 

Executes the rendering command for GPU spatial upscaling.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, XEG\_ExtensionProperties \*pProperties)

 | 

Queries XEngine Vulkan extensions.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateSpatialUpscale (VkDevice device, const XEG\_SpatialUpscaleCreateInfo \*pXegSpatialUpscaleCreateInfo, XEG\_SpatialUpscale \*pXegSpatialUpscale)

 | 

Creates an **XEG\_SpatialUpscale** object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_CmdRenderSpatialUpscale (VkCommandBuffer commandBuffer, XEG\_SpatialUpscale xegSpatialUpscale, XEG\_SpatialUpscaleDescription \*pXegSpatialUpscaleDescription)

 | 

Executes the rendering command for GPU spatial upscaling.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroySpatialUpscale (XEG\_SpatialUpscale xegSpatialUpscale)

 | 

Destroys an **XEG\_SpatialUpscale** object.

 |

#### Development Procedure

This section uses the OpenGL ES and Vulkan graphics APIs as examples to describe the XEngine integration process.

## Configuring Your Project

When compiling the HAP, add build dependency **libxengine.so** in the NDK for the .so files at the Native layer.

-   Referencing the header files
    
    Reference XEngine Kit's header files as required, for example, if your app needs to call OpenGL ES APIs to use the GPU spatial upscaling feature.
    
    #include <cstring>
    #include <cstdlib>
    #include <xengine/xeg\_gles\_extension.h>
    #include <xengine/xeg\_gles\_spatial\_upscale.h>
    
    Reference XEngine Kit's header files as required, for example, if your app needs to call Vulkan APIs to use the GPU spatial upscaling feature.
    
    #include <string>
    #include <vector>
    #include <algorithm>
    #include <xengine/xeg\_vulkan\_extension.h>
    #include <xengine/xeg\_vulkan\_spatial\_upscale.h>
    
-   Compiling CMakeLists.txt
    
    Reference the **CMakeLists** file of XEngine Kit as required, for example, when your app needs to call OpenGL ES APIs to use the GPU spatial upscaling feature. The following shows part of the sample code in **CMakeLists.txt**. You can find the complete sample code in [Demo (XEngine Kit-GLES)](https://gitee.com/harmonyos_samples/xengine-samplecode-gles-demo-cpp).
    
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
    
    Reference the **CMakeLists** file of XEngine Kit as required, for example, when your app needs to call Vulkan APIs to use the GPU spatial upscaling feature. The following shows part of the sample code in **CMakeLists.txt**. You can find the complete sample code in [Demo (XEngine Kit-Vulkan)](https://gitcode.com/harmonyos_samples/xengine-samplecode-vulkan-demo-cpp).
    
    find\_library(
        # Set the name of the path variable.
        xengine-lib
        # Specify the name of the NDK library that you want CMake to locate.
        xengine
    )
    find\_library(
        # Set the name of the path variable.
        Vulkan-lib
        # Specify the name of the NDK library that you want CMake to locate.
        vulkan
    )
    
    target\_link\_libraries(nativerender PUBLIC
    ${Vulkan-lib} ${xengine-lib})
    

## Integrating the GPU Spatial Upscaling Capability of XEngine Kit (OpenGL ES)

Set up the image rendering pipeline using EGL and OpenGL ES graphics APIs, and integrate GPU spatial upscaling at the Native layer. The rendering results are displayed on the screen through [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).

This section describes how to perform GPU spatial upscaling by calling OpenGL ES graphics APIs. You can find the complete sample code in [Demo (XEngine Kit-GLES)](https://gitcode.com/harmonyos_samples/xengine-samplecode-gles-demo-cpp).

Before calling XEngine Kit capabilities, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_GetString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_getstring) to obtain the extensions supported by XEngine. The GPU spatial upscaling APIs can be used only when the **XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME** extension is supported.
    
    // Query GLES extensions supported by XEngine.
    const char\* extensions = (const char\*)HMS\_XEG\_GetString(XEG\_EXTENSIONS);
    // Check whether the extensions support GPU spatial upscaling.
    if (!strstr(extensions, XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME)) {
        exit(1); // return error
    }
    

2.  Call [HMS\_XEG\_SpatialUpscaleParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_spatialupscaleparameter) to set parameters for GPU spatial upscaling.
    
    // **m\_sharpness** indicates the custom sharpening parameter. Here, its value is set to **0.3f** as an example.
    float m\_sharpness = 0.3f;
    // **m\_renderWidth** and **m\_renderHeight** respectively indicate the custom rendering width and height. Here, the resolution is set to 800 x 600 as an example.
    uint32\_t m\_renderWidth = 800;
    uint32\_t m\_renderHeight = 600;
    HMS\_XEG\_SpatialUpscaleParameter(XEG\_SPATIAL\_UPSCALE\_SHARPNESS, &m\_sharpness);
    // **upscaleScissor** indicates the sampling area of the upscaling input image.
    int upscaleScissor\[4\] = {0, 0, static\_cast<int>(m\_renderWidth), static\_cast<int>(m\_renderHeight)}; 
    HMS\_XEG\_SpatialUpscaleParameter(XEG\_SPATIAL\_UPSCALE\_SCISSOR, upscaleScissor);
    

3.  Call [HMS\_XEG\_RenderSpatialUpscale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_renderspatialupscale) to perform upscaling.
    
    // **upscaleFBO** indicates the custom framebuffer parameter.
    unsigned int upscaleFBO;
    glBindFramebuffer(GL\_FRAMEBUFFER, upscaleFBO); 
    // **m\_upscaleWidth** and **m\_upscaleHeight** respectively indicate the custom upscaling width and height. Here, the upscaling resolution is set to 1200 x 900 as an example.
    uint32\_t m\_upscaleWidth = 1200;
    uint32\_t m\_upscaleHeight = 900;
    glViewport(0, 0, m\_upscaleWidth, m\_upscaleHeight);
    glScissor(0, 0, m\_upscaleWidth, m\_upscaleHeight); 
    // **upscaleColorBuffer** indicates the texture attachment. You can customize this parameter as required.
    unsigned int upscaleColorBuffer;
    HMS\_XEG\_RenderSpatialUpscale(upscaleColorBuffer);
    
    **upscaleFBO** indicates the framebuffer you have created, which will be attached with the texture. The image will be drawn onto the texture after you call the upscaling API.
    

## Integrating the GPU Spatial Upscaling Capability of XEngine Kit (Vulkan)

Set up the image rendering pipeline using Vulkan graphics APIs, and integrate GPU spatial upscaling at the Native layer. The rendering results are displayed on the screen through [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).

This section describes how to perform GPU spatial upscaling by calling Vulkan graphics APIs. You can find the complete sample code in [Demo (XEngine Kit-Vulkan)](https://gitee.com/harmonyos_samples/xengine-samplecode-vulkan-demo-cpp).

Before calling XEngine Kit capabilities, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties) to obtain the extensions supported by XEngine. The GPU spatial upscaling APIs can be used only when the **XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME** extension is supported.
    
    // **physicalDevice** indicates a physical device defined by Vulkan and needs to be initialized.
    VkPhysicalDevice physicalDevice;
    // Query the Vulkan extensions supported by XEngine.
    std::vector<std::string> supportedExtensions;
    uint32\_t pPropertyCount;
    HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount, nullptr);
    if (pPropertyCount > 0) {
        std::vector<XEG\_ExtensionProperties> pProperties(pPropertyCount);
        if (HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount, &pProperties.front()) == VK\_SUCCESS) {
            for (auto ext : pProperties) {
    	    supportedExtensions.push\_back(ext.extensionName);
    	}
        }
    }
    // Check whether the extensions support GPU spatial upscaling.
    if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME) == supportedExtensions.end()) {
        exit(1); // return error
    }
    

2.  Declare the instance handle.
    
    XEG\_SpatialUpscale xegSpatialUpscale;
    
3.  Call [HMS\_XEG\_CreateSpatialUpscale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_createspatialupscale) to create an upscaling instance.
    
    // The rendering width and height, as well as the width and height after upscaling, are custom parameters. Here, we'll use an example of upscaling an 800 x 600 resolution to a 1200 x 900 resolution.
    uint32\_t m\_renderWidth = 800;
    uint32\_t m\_renderHeight = 600;
    uint32\_t m\_upscaleWidth = 1200;
    uint32\_t m\_upscaleHeight = 900;
    // Logical device defined by Vulkan, which needs to be initialized.
    VkDevice device;
    // **VkRect2D** indicates the 2D area structure specified by Vulkan.
    // **srcRect2D** indicates the upscaling input texture area. You can customize this parameter as required.
    VkRect2D srcRect2D;
    // **srcRect2D.offset.x** and **srcRect2D.offset.y** indicate the offset from the origin.
    srcRect2D.offset.x = 0;
    srcRect2D.offset.y = 0;
    // **srcRect2D.extent.width** and **srcRect2D.extent.height** indicate the width and height of the input texture.
    srcRect2D.extent.width = m\_renderWidth; 
    srcRect2D.extent.height = m\_renderHeight; 
    // **dstRect2D** indicates the upscaling output texture area. You can customize this parameter as required.
    VkRect2D dstRect2D;
    // **dstRect2D.offset.x** and **dstRect2D.offset.y** indicate the offset from the origin.
    dstRect2D.offset.x = 0;
    dstRect2D.offset.y = 0;
    // **dstRect2D.extent.width** and **dstRect2D.extent.height** indicate the width and height of the upscaling texture.
    dstRect2D.extent.width = m\_upscaleWidth; 
    dstRect2D.extent.height = m\_upscaleHeight; 
    XEG\_SpatialUpscaleCreateInfo createInfo;
    createInfo.format = VK\_FORMAT\_R8G8B8A8\_UNORM;
    // **sharpness** indicates the custom sharpening parameter. Here, its value is set to **0.3f** as an example.
    createInfo.sharpness = 0.3f;
    createInfo.outputSize = dstRect2D.extent;
    createInfo.inputRegion = srcRect2D;
    createInfo.outputRegion = dstRect2D;
    createInfo.inputSize = srcRect2D.extent;
    HMS\_XEG\_CreateSpatialUpscale(device, &createInfo, &xegSpatialUpscale);
    

4.  Call [HMS\_XEG\_CmdRenderSpatialUpscale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdrenderspatialupscale) to perform upscaling for each frame.
    
    // **inputImageView** indicates the **VkImageView** of the upscaling input image. You need to create this **VkImageView**.
    VkImageView inputImageView = VK\_NULL\_HANDLE; 
    // **outputImageView** indicates the **VkImageView** of the upscaling output image. You need to create this **VkImageView**.
    VkImageView outputImageView = VK\_NULL\_HANDLE;
    // **cmdBuff** indicates the command buffer and needs to be initialized.
    VkCommandBuffer cmdBuff = VK\_NULL\_HANDLE ;
    XEG\_SpatialUpscaleDescription xegDescription;
    xegDescription.inputImage = inputImageView; 
    xegDescription.outputImage = outputImageView; 
    HMS\_XEG\_CmdRenderSpatialUpscale(cmdBuff, xegSpatialUpscale, &xegDescription);
    

5.  Call [HMS\_XEG\_DestroySpatialUpscale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_destroyspatialupscale) to destroy the instance.
    
    HMS\_XEG\_DestroySpatialUpscale(xegSpatialUpscale);
