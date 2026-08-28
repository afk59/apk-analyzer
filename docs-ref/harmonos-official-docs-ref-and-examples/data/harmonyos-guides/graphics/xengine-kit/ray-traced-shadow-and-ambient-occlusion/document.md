# Ray-Traced Shadow and Ambient Occlusion

Since version 6.0.0 (20), the Ray-Traced Shadow and Ambient Occlusion (AO) capabilities are supported.

The VisibleMask feature of XEngine provides out-of-the-box Ray-Traced Shadow and AO rendering capabilities. Compared with traditional ray tracing implementations of these effects, XEngine Kit leverages hardware-software co-optimization on the Maleoon GPU to support the Flexible Entry Raytracing (FERT) intersection acceleration technology. This reduces the number of ray-geometry intersection calculations, thereby lowering GPU workload while delivering high-quality ray tracing effects. In addition, XEngine Kit uses the highly optimized temporal-spatial denoising technology to solve the noise issue introduced by insufficient rays during ray tracing rendering. This technology achieves high image quality with a small number of rays, lighter GPU workload for the same image quality, and better image quality under the same workload.

#### Restrictions

-   Devices need to support Vulkan ray tracing extensions [VK\_KHR\_acceleration\_structure](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_acceleration_structure.html) and [VK\_KHR\_ray\_query](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_ray_query.html).
-   You can check whether the relevant extension is supported as follows:
    
    For Vulkan, use the extension query API [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties). If the query result contains **XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME**, the extension is supported; otherwise, the extension is not supported.
    

#### API Description

The following APIs are required for using the Ray-Traced Shadow and Ambient Occlusion features. For details about these APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine).

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \* pPropertyCount, XEG\_ExtensionProperties \* pProperties)

 | 

Queries XEngine Vulkan extensions.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateRTVisibleMask (VkDevice device, const void \*pCreateInfo, XEG\_RTVisibleMask \*pRTVisibleMask)

 | 

Creates an **XEG\_RTVisibleMask** object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRenderRTVisibleMask (VkCommandBuffer commandBuffer, XEG\_RTVisibleMask rtVisibleMask, const void \*pDescription)

 | 

Records the ray-traced VisibleMask rendering command.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyRTVisibleMask (XEG\_RTVisibleMask rtVisibleMask)

 | 

Destroys an **XEG\_RTVisibleMask** object.

 |

#### Development Procedure

This section uses the integration in the deferred rendering pipeline of the Vulkan app as an example to describe how to develop the Ray-Traced Shadow and Ambient Occlusion features of XEngine.

## Configuring Your Project

During HAP compilation, the native .so files depend on the XEngine-related libraries and header files in the NDK.

-   Referencing the header files
    
    #include <vector>
    #include <algorithm>
    #include <string>
    #include <xengine/xeg\_vulkan\_extension.h>
    #include <xengine/xeg\_vulkan\_rt\_visible\_mask.h>
    
-   Adding library dependencies to CMakeLists.txt
    
    Add the following code to **CMakeLists.txt** to add the dependency on the XEngine dynamic link library. .
    
    find\_library(
        # Set the name of the path variable.
        xengine-lib
        # Specify the name of the NDK library that you want CMake to locate.
        xengine
    )
    target\_link\_libraries(nativerender PUBLIC
        ...... // Other library files.
        ${xengine-lib})
    

## Integrating XEngine Ray-Traced Shadow and Ambient Occlusion (Vulkan)

The effect APIs for Ray-Traced Shadow (RTShadow) and Ray-Traced Ambient Occlusion (RTAO) of XEngine's VisibleMask feature need to work with the Vulkan API deferred rendering pipeline. The related code is implemented at the Native layer, and the rendering result is displayed on the screen through [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).

Before calling the feature APIs of XEngine Kit, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties) to obtain the extensions supported by XEngine. The Ray-Traced Shadow and Ambient Occlusion APIs can be used only when the **XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME** extension is supported.
    
    // **physicalDevice** indicates the Vulkan physical device of the current app and needs to be initialized.
    VkPhysicalDevice physicalDevice;
    // Query the Vulkan extensions supported by XEngine.
    std::vector<std::string> supportedExtensions;
    uint32\_t propertyCount;
    HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, nullptr);
    if (propertyCount > 0) {
        std::vector<XEG\_ExtensionProperties> properties(propertyCount);
        if (HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, &properties.front())
            == VK\_SUCCESS) {
            for (auto ext : properties) {
                supportedExtensions.push\_back(ext.extensionName);
            }
        }
    }
    // Query whether the Ray-Traced Shadow and Ambient Occlusion features of XEngine are supported.
    if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG\_RT\_SHADOW\_AO\_EXTENSION\_NAME)
        == supportedExtensions.end()) {
        exit(1); // Handle the error if not supported.
    }
    
2.  Call [HMS\_XEG\_CreateRTVisibleMask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_creatertvisiblemask) to create an instance handle.
    
    // Declare the instance handle.
    XEG\_RTVisibleMask rtVisibleMask = VK\_NULL\_HANDLE;
    // RTShadow and RTAO initialization information.
    XEG\_RTShadowAOCreateInfo createInfo;
    createInfo.sType = XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_CREATE\_INFO;
    createInfo.pNext = nullptr;
    // GBuffer image size.
    createInfo.rtInputGbufferSize = {1280, 720};
    // Sizes of the output RTShadow and RTAO images, which must be in the same ratio as the GBuffer.
    createInfo.rtShadowAOSize = {640, 360};
    createInfo.enableRTShadow = true;
    createInfo.enableRTAO = true;
    // Set the denoising quality mode to Balanced mode.
    createInfo.denoiseMode = XEG\_DENOISE\_QUALITY\_MODE\_BALANCED;
    // Set the scene traversal mode to Performance mode.
    createInfo.traversalMode = XEG\_TRAVERSAL\_MODE\_PERFORMANCES;
    createInfo.aoOnlyInShadow = false;
    createInfo.reverseZ = false;
    // **device** indicates the Vulkan device object of the current app and needs to be initialized.
    VkDevice device;
    if (HMS\_XEG\_CreateRTVisibleMask(device, &createInfo, &rtVisibleMask) != VK\_SUCCESS) {
        exit(1);  // Handle the error if the creation failed.
    }
    
3.  Call [HMS\_XEG\_CmdRenderRTVisibleMask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdrenderrtvisiblemask) to execute the rendering command for each frame.
    
    // Set RTShadow algorithm parameters.
    XEG\_RTShadowParameters shadowParameters;
    // Set RTAO algorithm parameters.
    XEG\_RTAOParameters aoParameters;
    // Set the denoiser parameters.
    XEG\_RTShadowAODenoiserParameters denoiserParameters;
    // RTShadow and RTAO rendering input information.
    XEG\_RTShadowAODescription description;
    // Only opaque objects are considered for ray intersection.
    const uint32\_t gl\_RayFlagsOpaqueEXT = 1U;
    // Stop the ray intersection query when the first intersection point is found.
    const uint32\_t gl\_RayFlagsTerminateOnFirstHitEXT = 4U;
    const uint32\_t rayFlags = (gl\_RayFlagsOpaqueEXT | gl\_RayFlagsTerminateOnFirstHitEXT) << 8;
    
    shadowParameters.rayTMax = 200.0f;
    shadowParameters.rayTMin = 1.0f;
    shadowParameters.sunDirection\[0\] = 0.1;
    shadowParameters.sunDirection\[1\] = 0.1;
    shadowParameters.sunDirection\[2\] = 0.1;
    shadowParameters.raySourceAngleInDegree = 0.35f;
    shadowParameters.shadowCullMask = rayFlags | 0xFF;
    shadowParameters.shadowCullDistance = 2000.0f;
    
    aoParameters.rayTMax = 30.0f;
    aoParameters.rayTMin = 0.1f;
    aoParameters.aoIntensity = 0.8f;
    aoParameters.aoNormalBias = 0.5f;
    aoParameters.aoCullMask = rayFlags | 0xFF;
    aoParameters.aoCullDistance = 2000.0f;
    
    denoiserParameters.temporalBlendFactor = 0.75f;
    denoiserParameters.positionConstantDistance = 5.0f;
    denoiserParameters.spatialDenoiseTimes = 2;
    denoiserParameters.ghostingAlpha = 0.5;
    denoiserParameters.spatialNormalWeight = 0.0f;
    denoiserParameters.spatialMaxKernelStep = 1;
    
    description.sType = XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_DESCRIPTION;
    description.pNext = nullptr;
    description.worldCameraOrigin\[0\] = 0.0; // The x coordinate of the camera's actual position is used.
    description.worldCameraOrigin\[1\] = 0.0; // The y coordinate of the camera's actual position is used.
    description.worldCameraOrigin\[2\] = 0.0; // The z coordinate of the camera's actual position is used.
    // **gBufferDepth** indicates the **VkImageView** of the GBuffer depth image and needs to be initialized.
    VkImageView gBufferDepth;
    description.inputDepthImage = gBufferDepth;
    // **gBufferNormal** indicates the **VkImageView** of the GBuffer normal image and needs to be initialized. For details about the normal format and encoding, please refer to API Reference.
    VkImageView gBufferNormal;
    description.inputNormalImage = gBufferNormal;
    // **outputShadowAOView** indicates the **VkImageView** that stores the rendering output of XEngine RTShadow and RTAO, and needs to be initialized.
    VkImageView outputShadowAOView;
    description.outputShadowAOImage = outputShadowAOView;
    // **sceneTlas** indicates the top-level ray tracing acceleration structure of the scene and needs to be initialized.
    VkAccelerationStructureKHR sceneTlas;
    description.accelerationStructure = sceneTlas;
    float viewMatrix\[16\]; // Camera view matrix, which needs to be initialized.
    float projectionMatrix\[16\]; // Camera projection matrix, which needs to be initialized.
    memcpy(description.viewMatrix, viewMatrix, sizeof(viewMatrix));
    memcpy(description.projectionMatrix, projectionMatrix, sizeof(projectionMatrix));
    VkCommandBuffer vkCommandBuffer; // Vulkan command buffer, which needs to be initialized.
    VkResult ret = HMS\_XEG\_CmdRenderRTVisibleMask(vkCommandBuffer, rtVisibleMask, &description);
    if (ret != VK\_SUCCESS) {
        // Handle any command recording error.
    }
    // Set the pipeline barrier to synchronize the read access to the RTShadow and RTAO rendering output.
    VkImageMemoryBarrier imageMemoryBarrier;
    imageMemoryBarrier.sType = VK\_STRUCTURE\_TYPE\_IMAGE\_MEMORY\_BARRIER;
    imageMemoryBarrier.pNext = nullptr;
    imageMemoryBarrier.srcAccessMask = VK\_ACCESS\_COLOR\_ATTACHMENT\_WRITE\_BIT;
    imageMemoryBarrier.dstAccessMask = VK\_ACCESS\_COLOR\_ATTACHMENT\_READ\_BIT; // Perform settings based on the actual access mode.
    imageMemoryBarrier.oldLayout = VK\_IMAGE\_LAYOUT\_COLOR\_ATTACHMENT\_OPTIMAL;
    imageMemoryBarrier.newLayout = VK\_IMAGE\_LAYOUT\_SHADER\_READ\_ONLY\_OPTIMAL;
    imageMemoryBarrier.srcQueueFamilyIndex = VK\_QUEUE\_FAMILY\_IGNORED;
    imageMemoryBarrier.dstQueueFamilyIndex = VK\_QUEUE\_FAMILY\_IGNORED;
    VkImage outputShadowAOImage; // **outputShadowAO** indicates the **VkImage** that stores the rendering output of RTShadow and RTAO, and needs to be initialized.
    imageMemoryBarrier.image = outputShadowAOImage; 
    imageMemoryBarrier.subresourceRange = { VK\_IMAGE\_ASPECT\_COLOR\_BIT, 0, 1, 0, 1 };
    vkCmdPipelineBarrier(vkCommandBuffer, 
        VK\_PIPELINE\_STAGE\_COLOR\_ATTACHMENT\_OUTPUT\_BIT, 
        VK\_PIPELINE\_STAGE\_FRAGMENT\_SHADER\_BIT, // Perform settings based on the actual access stage.
        0, 0, nullptr, 0, nullptr, 1, &imageMemoryBarrier);
    
    The following shader code snippet example demonstrates how to compute the color of the shading point when **outputShadowAOImage** (RTShadow and RTAO rendering output) is applied to the lighting computation process.
    
    // lighting\_pass.frag code
    layout (binding = 0) uniform sampler2D textureRayTracingOutputShadowAO;
    
    // **color** indicates the color value of the current shading point when RTShadow and RTAO are not considered.
    vec3 color;
    // Color calculation process of the shading point...
    // Apply RTShadow and RTAO to the final illumination result.
    vec2 shadowAO = texture(textureRayTracingOutputShadowAO, TexCoords).xy;
    float shadow = shadowAO.x;
    float ao = shadowAO.y;
    vec3 finalColor = color \* pow(ao, 2.0) \* shadow; // **finalColor** indicates the final color value.
    
4.  Call [HMS\_XEG\_DestroyRTVisibleMask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_destroyrtvisiblemask) to destroy the feature instance handle to release resources when the feature is no longer used or the app exits.
    
    if (rtVisibleMask != VK\_NULL\_HANDLE) {
        HMS\_XEG\_DestroyRTVisibleMask(rtVisibleMask);
    }
