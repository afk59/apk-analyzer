# Ray-Traced Reflections

Since version 6.0.0(20), the Ray-Traced Reflections feature is supported.

XEngine Kit provides the Ray-Traced Reflections rendering capability. Compared with traditional ray tracing implementations of this effect, XEngine Kit leverages hardware-software co-optimization on the Maleoon GPU to support the Flexible Entry Raytracing (FERT) intersection acceleration technology. This reduces the number of ray-geometry intersection calculations, thereby lowering GPU workload while delivering high-quality ray tracing effects.

#### Restrictions

-   Devices need to support Vulkan ray tracing extensions [VK\_KHR\_acceleration\_structure](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_acceleration_structure.html) and [VK\_KHR\_ray\_query](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_ray_query.html).
-   You can check whether the relevant extension is supported as follows:
    
    For Vulkan, use the extension query API [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties). If the query result contains **XEG\_RT\_REFLECTION\_EXTENSION\_NAME**, the extension is supported; otherwise, the extension is not supported.
    

#### API Description

The following APIs are required for using the Ray-Traced Reflections feature. For details about these APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine).

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

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateRTReflection(VkDevice device, const void\* pCreateInfo, XEG\_RTReflection\* pRtReflection)

 | 

Creates an **XEG\_RTReflection** object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRenderRTReflection(VkCommandBuffer commandBuffer, XEG\_RTReflection rtReflection, const void\* pDescription)

 | 

Records the command for calculating the ray-traced reflection hit information.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyRTReflection(XEG\_RTReflection rtReflection)

 | 

Destroys an **XEG\_RTReflection** object.

 |

#### Development Procedure

This section uses the Vulkan app as an example to describe the XEngine integration process.

## Configuring Your Project

When compiling the HAP, add build dependency **libxengine.so** in the NDK for the .so files at the Native layer.

-   Referencing the header files
    
    #include <algorithm>
    #include <string>
    #include <vector>
    #include "xengine/xeg\_vulkan\_extension.h"
    #include <xengine/xeg\_vulkan\_rt\_reflection.h>
    
-   Compiling CMakeLists.txt
    
    The following shows part of the sample code in **CMakeLists.txt**.
    
    find\_library(
        # Set the name of the path variable.
        xengine-lib
        # Specify the name of the NDK library that you want CMake to locate.
        xengine
    )
    target\_link\_libraries(nativerender PUBLIC
        ...... // Other library files.
        ${xengine-lib})
    

## Integrating XEngine Ray-Traced Reflections (Vulkan)

Set up the image rendering pipeline using Vulkan graphics APIs, and integrate the code for the ray-traced reflection effect at the Native layer. The rendering results are displayed on the screen through [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).

Before calling XEngine Kit capabilities, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties) to obtain the extensions supported by XEngine. The Ray-Traced Reflections APIs can be used only when the **XEG\_RT\_REFLECTION\_EXTENSION\_NAME** extension is supported.
    
    // **physicalDevice** indicates a physical device defined by Vulkan and needs to be initialized.
    VkPhysicalDevice physicalDevice;
    // Query the Vulkan extensions supported by XEngine.
    std::vector<std::string> supportedExtensions;
    uint32\_t propertyCount;
    HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, nullptr);
    if (propertyCount > 0) {
        std::vector<XEG\_ExtensionProperties> properties(propertyCount);
        if (HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, &properties.front()) == VK\_SUCCESS) {
            for (auto ext : properties) {
                supportedExtensions.push\_back(ext.extensionName);
            }
        }
    }
    // Query whether the Ray-Traced Reflections feature is supported.
    if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG\_RT\_REFLECTION\_EXTENSION\_NAME) ==
        supportedExtensions.end()) {
        exit(1); // Error.
    }
    
2.  Declare the instance handle.
    
    XEG\_RTReflection xegRTReflection;
    
3.  Call [HMS\_XEG\_CreateRTReflection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_creatertreflection) to create a ray-traced reflection instance.
    
    // The width and height information required for creating a ray-traced reflection instance are custom parameters. The following uses the 800 x 600 resolution as an example.
    uint32\_t reflectWidth = 800;
    uint32\_t reflectHeight = 600;
    // Logical device defined by Vulkan, which needs to be initialized.
    VkDevice device;
    // **XEG\_RTReflectionCreateInfo** indicates the information required for creating an **xegRTReflection** object.
    XEG\_RTReflectionCreateInfo xegRTReflectionCreateInfo;
    // Set whether to enable the fast intersection mode. The default value is **0**, indicating that the mode is disabled.
    xegRTReflectionCreateInfo.enableFastTrace = 0;
    // Set **XEG\_StructureType**. The value must be **XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO**.
    xegRTReflectionCreateInfo.sType = XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO;
    // Specify the input image dimensions.
    xegRTReflectionCreateInfo.renderSize = VkExtent2D{ reflectWidth, reflectHeight };
    VkResult ret = HMS\_XEG\_CreateRTReflection(device, &xegRTReflectionCreateInfo, &xegRTReflection);
    if (ret != VK\_SUCCESS) {
        exit(1);  // Error.
    }
    
4.  Call [HMS\_XEG\_CmdRenderRTReflection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdrenderrtreflection) to send the rendering command for each frame.
    
    // Reflection rendering input information.
    XEG\_RTReflectionDescription xegRTReflectionDescription;
    // **inputRayOriginImage** indicates the **VkImageView** of the ray origin image. You need to create this **VkImageView**.
    VkImageView inputRayOriginImage = VK\_NULL\_HANDLE;
    // **inputRayDirectionImage** indicates the **VkImageView** of the ray direction image. You need to create this **VkImageView**.
    VkImageView inputRayDirectionImage = VK\_NULL\_HANDLE;
    // **outputReflectionInfoImage** indicates the **VkImageView** for recording the ray tracing intersection result. You need to create this **VkImageView**.
    VkImageView outputReflectionInfoImage = VK\_NULL\_HANDLE;
    // **sceneTlas** indicates the top-level ray tracing acceleration structure of the scene.
    VkAccelerationStructureKHR sceneTlas = VK\_NULL\_HANDLE;
    xegRTReflectionDescription.inputRayOriginImage = inputRayOriginImage;
    xegRTReflectionDescription.inputRayDirectionImage = inputRayDirectionImage;
    xegRTReflectionDescription.outputReflectionInfoImage = outputReflectionInfoImage;
    xegRTReflectionDescription.accelerationStructure = sceneTlas;
    xegRTReflectionDescription.rayMin = 0.01;
    xegRTReflectionDescription.rayMax = 1e10;
    xegRTReflectionDescription.sType = XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_DESCRIPTION;
    xegRTReflectionDescription.reflectionCullMask = 0xff;
    // **commandBuffer** indicates the command buffer and needs to be initialized.
    VkCommandBuffer commandBuffer = VK\_NULL\_HANDLE;
    VkResult retRender = HMS\_XEG\_CmdRenderRTReflection(commandBuffer, xegRTReflection, &xegRTReflectionDescription);
    if (retRender != VK\_SUCCESS) {
        exit(1); // Error.
    }
    
5.  Call [HMS\_XEG\_DestroyRTReflection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_destroyrtreflection) to destroy the instance and release resources when the feature is no longer used or the app exits.
    
    if (xegRTReflection != VK\_NULL\_HANDLE) {
        HMS\_XEG\_DestroyRTReflection(xegRTReflection);
    }
