# Adaptive VRS

XEngine Kit offers adaptive VRS capability, which optimizes resource allocation, reducing the rendering frequency without visual loss. This allows for varying rendering rates for different images, effectively improving rendering performance.

#### Restrictions

-   Phones are supported. Additionally, tablets and PCs/2-in-1 devices are supported since version 5.0.2(14), and TVs are supported since version 5.1.0(18).
-   You can check whether the relevant extension is supported as follows:
    
    For OpenGL ES, use the extension query API [HMS\_XEG\_GetString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_getstring). If the query result contains [XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#xeg_adaptive_vrs_extension_name), the extension is supported; otherwise, the extension is not supported.
    

#### API Description

The following lists APIs for adaptive VRS setting. For details about more setting and query APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine).

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

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_AdaptiveVRSParameter (GLenum pname, GLvoid \* param)

 | 

Sets adaptive VRS parameters.

 |
| 

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_DispatchAdaptiveVRS (GLfloat \* reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage)

 | 

Computes the shading rate image.

 |
| 

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_ApplyAdaptiveVRS (GLuint shadingRateImage)

 | 

Applies the shading rate image to the render target.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \* pPropertyCount, XEG\_ExtensionProperties \* pProperties)

 | 

Queries XEngine Vulkan extensions.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateAdaptiveVRS (VkDevice device, XEG\_AdaptiveVRSCreateInfo \* pXegAdaptiveVRSCreateInfo, XEG\_AdaptiveVRS \* pXegAdaptiveVRS)

 | 

Creates an **XEG\_AdaptiveVRS** object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_CmdDispatchAdaptiveVRS (VkCommandBuffer commandBuffer, XEG\_AdaptiveVRS xegAdaptiveVRS, XEG\_AdaptiveVRSDescription \* pXegAdaptiveVRSDescription)

 | 

Executes the command for computing the adaptive VRS.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyAdaptiveVRS (XEG\_AdaptiveVRS xegAdaptiveVRS)

 | 

Destroys an **XEG\_AdaptiveVRS** object.

 |

#### Development Procedure

This section uses the OpenGL ES and Vulkan graphics APIs as examples to describe the XEngine integration process.

## Configuring Your Project

When compiling the HAP, add build dependency **libxengine.so** in the NDK for the .so files at the Native layer.

-   Referencing the header files
    
    Reference XEngine Kit's header files as required, for example, if your app needs to call OpenGL ES APIs to use the adaptive VRS feature.
    
    #include <cstring>
    #include <cstdlib>
    #include <xengine/xeg\_gles\_extension.h>
    #include <xengine/xeg\_gles\_adaptive\_vrs.h>
    
    Reference XEngine Kit's header files as required, for example, if your app needs to call Vulkan APIs to use the adaptive VRS feature.
    
    #include <string>
    #include <vector>
    #include <algorithm>
    #include <xengine/xeg\_vulkan\_extension.h>
    #include <xengine/xeg\_vulkan\_adaptive\_vrs.h>
    
-   Compiling CMakeLists.txt
    
    Reference the **CMakeLists** file of XEngine Kit as required, for example, when your app needs to call OpenGL ES APIs to use the adaptive VRS feature. The following shows part of the sample code in **CMakeLists.txt**. You can find the complete sample code in [Demo (XEngine Kit-GLES)](https://gitcode.com/harmonyos_samples/xengine-samplecode-gles-demo-cpp).
    
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
    
    Reference the **CMakeLists** file of XEngine Kit as required, for example, when your app needs to call Vulkan APIs to use the adaptive VRS feature. The following shows part of the sample code in **CMakeLists.txt**. You can find the complete sample code in [Demo (XEngine Kit-Vulkan)](https://gitee.com/harmonyos_samples/xengine-samplecode-vulkan-demo-cpp).
    
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
    

## Integrating Adaptive VRS (OpenGL ES)

The creation and binding of shading rate textures in the adaptive VRS feature (OpenGL ES version) are implemented through the APIs provided by relevant extensions.

Before calling XEngine Kit capabilities, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_GetString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_getstring) to obtain the extensions supported by XEngine. The adaptive VRS APIs can be used only when the [XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#xeg_adaptive_vrs_extension_name) extension is supported.
    
    // Query GLES extensions supported by XEngine.
    const char\* extensions = (const char\*)HMS\_XEG\_GetString(XEG\_EXTENSIONS);
    // Check whether the extensions support adaptive VRS.
    if (!strstr(extensions, XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME)) {
        exit(1); // return error
    }
    

2.  Call [HMS\_XEG\_AdaptiveVRSParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_adaptivevrsparameter) to set the parameters for adaptive VRS.
    
    // **renderWidth** and **renderHeight** respectively indicate the custom rendering width and height. Here, the resolution is set to 800 x 600 as an example.
    uint32\_t renderWidth = 800;
    uint32\_t renderHeight = 600;
    // **inputSize** indicates the image size finally rendered by the rendering pipeline of the previous frame. You can customize this parameter as required.
    GLsizei inputSize\[2\] = {static\_cast<GLsizei>(renderWidth), static\_cast<GLsizei>(renderHeight)};
    HMS\_XEG\_AdaptiveVRSParameter(XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE, inputSize);
    // **inputRegion** indicates the image region finally rendered by the rendering pipeline of the previous frame. You can customize this parameter as required.
    GLuint inputRegion\[4\] = {0, 0, renderWidth, renderHeight};
    HMS\_XEG\_AdaptiveVRSParameter(XEG\_ADAPTIVE\_VRS\_INPUT\_REGION, inputRegion);
    // **texelSizes** indicates the tile size for rendering. The options are \[8, 8\] and \[16, 16\].
    GLsizei texelSizes\[2\] = {8, 8};
    HMS\_XEG\_AdaptiveVRSParameter(XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE, texelSizes);
    // **sensitivity** indicates the threshold for controlling the generation of the shading rate image. The recommended value range is \[0, 1\].
    GLfloat sensitivity = 0.15;
    HMS\_XEG\_AdaptiveVRSParameter(XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY, &sensitivity);
    // **flip** indicates whether to flip an image up or down (**true**: flip; **false**: not flip). Here, the value is set to **false** as an example.
    GLboolean flip = false;
    HMS\_XEG\_AdaptiveVRSParameter(XEG\_ADAPTIVE\_VRS\_FLIP, &flip);
    
3.  Call [HMS\_XEG\_DispatchAdaptiveVRS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_dispatchadaptivevrs) to compute the shading rate image.
    
    // **inputColorImage** indicates the texture of the color attachment containing the final rendering result of the rendering pipeline of the previous frame. You can customize this parameter as required.
    GLuint inputColorImage; 
    // **inputDepthImage** indicates the texture of the depth attachment containing the final rendering result of the rendering pipeline of the current frame. You can customize this parameter as required.
    GLuint inputDepthImage;
    // **outputShadingRateImage** indicates the texture used to generate the shading rate image information. You can customize this parameter as required.
    GLuint outputShadingRateImage;
    // **reprojectionMatrix** indicates the reprojection matrix computed based on the projection matrix and view matrix.
    float \*reprojectionMatrix = nullptr; 
    HMS\_XEG\_DispatchAdaptiveVRS(reprojectionMatrix, inputColorImage, inputDepthImage, outputShadingRateImage);
    

4.  Call [HMS\_XEG\_ApplyAdaptiveVRS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_applyadaptivevrs) to apply the shading rate image to the render target.
    
    HMS\_XEG\_ApplyAdaptiveVRS(outputShadingRateImage);
    

## Integrating Adaptive VRS (Vulkan)

Before calling XEngine Kit capabilities, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties) to obtain the extensions supported by XEngine. The adaptive VRS APIs can be used only when the [XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#xeg_adaptive_vrs_extension_name) extension is supported.
    
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
    // Check whether the extensions support adaptive VRS.
    if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME) == supportedExtensions.end()) {
    	exit(1); // return error
    }
    
2.  Declare the instance handle.
    
    XEG\_AdaptiveVRS xeg\_adaptiveVRS;
    
3.  Call [HMS\_XEG\_CreateAdaptiveVRS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_createadaptivevrs) to define and create an instance.
    
    // **m\_renderWidth** and **m\_renderHeight** indicate the texture sampling width and height, respectively.
    int m\_renderWidth;
    int m\_renderHeight;
    // **VRS\_TILE\_SIZE** indicates the tile size for adaptive VRS rendering.
    int VRS\_TILE\_SIZE;
    // Logical device defined by Vulkan, which needs to be initialized.
    VkDevice device;
    // **XEG\_AdaptiveVRSCreateInfo** indicates the parameter information of the adaptive VRS instance handle object.
    XEG\_AdaptiveVRSCreateInfo xeg\_createInfo;
    // **XEG\_AdaptiveVRSDescription** indicates the parameter information required for sending the command for drawing the shading rate texture.
    XEG\_AdaptiveVRSDescription xeg\_description;
    // **VkExtent2D inputSize** indicates the image size finally rendered by the rendering pipeline of the previous frame. You can customize this parameter as required.
    VkExtent2D inputSize;
    inputSize.width = m\_renderWidth;
    inputSize.height = m\_renderHeight;
    // **VkRect2D** indicates the 2D area structure specified by Vulkan.
    // **inputRegion** indicates the input texture area for adaptive VRS. You can customize this parameter as required.
    VkRect2D inputRegion {};
    // **inputRegion.extent.width** and **inputRegion.extent.height** indicate the texture sampling width and height, respectively.
    inputRegion.extent.width = m\_renderWidth;
    inputRegion.extent.height = m\_renderHeight;
    // **inputRegion.offset.x** and **inputRegion.offset.y** indicate the offset from the origin.
    inputRegion.offset.x = 0;
    inputRegion.offset.y = 0;
    // **xeg\_createInfo.inputSize** indicates the image size finally rendered by the rendering pipeline of the previous frame.
    xeg\_createInfo.inputSize = inputSize;
    // **xeg\_createInfo.inputRegion** indicates the image region finally rendered by the rendering pipeline of the previous frame.
    xeg\_createInfo.inputRegion = inputRegion;
    // **xeg\_createInfo.adaptiveTileSize** indicates the tile size for adaptive VRS rendering.
    xeg\_createInfo.adaptiveTileSize = VRS\_TILE\_SIZE;
    // **xeg\_createInfo.errorSensitivity** indicates the threshold for generating the final shading rate texture result. Here, the threshold is set to **0.5** as an example.
    xeg\_createInfo.errorSensitivity = 0.5;
    // **xeg\_createInfo.flip** indicates whether to flip an image up or down (**true**: flip; **false**: not flip). Here, the value is set to **false** as an example.
    xeg\_createInfo.flip = false;
    HMS\_XEG\_CreateAdaptiveVRS(device, &xeg\_createInfo, &xeg\_adaptiveVRS);
    

4.  Call [HMS\_XEG\_CmdDispatchAdaptiveVRS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmddispatchadaptivevrs) to send the adaptive VRS command and generate the shading rate texture per image.
    
    // **inputColorImageView** indicates the custom texture of the color attachment containing the final rendering result of the rendering pipeline of the previous frame.
    VkImageView inputColorImageView = VK\_NULL\_HANDLE;
    // **inputDepthImageView** indicates the custom texture of the depth attachment containing the final rendering result of the rendering pipeline of the current frame.
    VkImageView inputDepthImageView = VK\_NULL\_HANDLE;
    // **outputShadingRateImage** indicates the custom texture used to generate the shading rate image information.
    VkImageView outputShadingRateImage = VK\_NULL\_HANDLE;
    // **cmdBuff** indicates the command buffer and needs to be initialized.
    VkCommandBuffer commandBuffer = VK\_NULL\_HANDLE ;
    xeg\_description.inputColorImage = inputColorImageView; 
    xeg\_description.inputDepthImage = inputDepthImageView;
    xeg\_description.outputShadingRateImage = outputShadingRateImage;
    // **xeg\_description.reprojectionMatrix** indicates the reprojection matrix computed based on the projection matrix and view matrix.
    xeg\_description.reprojectionMatrix = nullptr; 
    HMS\_XEG\_CmdDispatchAdaptiveVRS(commandBuffer, xeg\_adaptiveVRS, &xeg\_description);
    

5.  Call [HMS\_XEG\_DestroyAdaptiveVRS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_destroyadaptivevrs) to uninstall the VRS instance and clear VRS-related resources.
    
    HMS\_XEG\_DestroyAdaptiveVRS(xeg\_adaptiveVRS);
