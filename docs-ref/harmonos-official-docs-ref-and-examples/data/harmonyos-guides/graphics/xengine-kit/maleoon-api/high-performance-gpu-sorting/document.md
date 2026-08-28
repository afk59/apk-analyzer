# High-Performance GPU Sorting

Since version 6.0.0(20), the High-Performance GPU Sorting feature is supported.

The HPS feature of XEngine Kit provides the high-performance GPU sorting capability. Compared with other sorting capabilities, this capability relies on the hardware-software co-optimization of Maleoon GPU.

#### Restrictions

You can check whether the relevant extension is supported as follows:

For Vulkan, use the extension query API [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties). If the query result contains **XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME**, the extension is supported; otherwise, the extension is not supported.

#### API Description

The following APIs are required for high-performance GPU sorting. For details about these APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine).

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateHPS (VkDevice device, const XEG\_HPSCreateInfo \*pCreateInfo, XEG\_HPS \*pHps)

 | 

Creates an **XEG\_HPS** object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyHPS (XEG\_HPS hps)

 | 

Destroys an **XEG\_HPS** object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRadixSortHPS (VkCommandBuffer commandBuffer, XEG\_HPS hps, const XEG\_HPSRadixSortDescription \*pDescription)

 | 

Records an HPS radix sort command. Before using this API, you need to call **HMS\_XEG\_EnumerateDeviceExtensionProperties** to check whether the **XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME** extension is supported.

 |

#### Development Procedure

This section uses Vulkan app rendering as an example to describe how to develop high-performance GPU sorting.

## Configuring Your Project

During HAP compilation, the native .so files depend on the XEngine-related libraries and header files in the NDK.

-   Referencing the header files
    
    #include <algorithm>
    #include <vector>
    #include <string>
    #include <xengine/xeg\_vulkan\_hps.h>
    #include <xengine/xeg\_vulkan\_extension.h>
    #include <xengine/xeg\_extension\_defs.h>
    
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
    

## Integrating High-Performance GPU Sorting (Vulkan)

XEngine high-performance GPU sorting can be used independently. The related code is implemented at the Native layer.

Before calling the feature APIs of XEngine Kit, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties) to obtain the extensions supported by XEngine. The high-performance GPU sorting APIs can be used only when the **XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME** extension is supported.
    
    VkPhysicalDevice physicalDevice;
    std::vector<std::string> supportedExtensions;
    uint32\_t propertyCount;
    HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, nullptr);
    if (propertyCount > 0) {
        std::vector<XEG\_ExtensionProperties> properties(propertyCount);
        if (HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, &properties.front()) ==
            VK\_SUCCESS) {
            for (auto ext : properties) {
                supportedExtensions.push\_back(ext.extensionName);
            }
        }
    }
    if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME) ==
        supportedExtensions.end()) {
        exit(1);
    }
    
2.  Prepare HPS resources.
    
    VkDevice device;
    VkCommandBuffer cmdBuffer;
    VkQueue queue;
    // Key to be sorted.
    VkBuffer keyBuffer;
    // Value corresponding to the key.
    VkBuffer indexBuffer;
    // Sorting amount.
    VkBuffer sortCount;
    
3.  Declare the instance handle.
    
    XEG\_HPS xegHPS { VK\_NULL\_HANDLE };
    
4.  Call [HMS\_XEG\_CreateHPS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_createhps) to instantiate the handle.
    
    // Construct the input descriptor.
    XEG\_HPSRadixSort sorInfo{
        XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT,
        nullptr
    };
    
    XEG\_HPSCreateInfo info {
        XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO, 
        &sorInfo
    };
    // Instantiate the handle.
    HMS\_XEG\_CreateHPS(device, &info, &xegHPS);
    
5.  Construct a sorting descriptor and call [HMS\_XEG\_CmdRadixSortHPS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdradixsorthps) to record the radix sort command.
    
    VkCommandBufferBeginInfo cmdBufferBeginInfo {};
    cmdBufferBeginInfo.sType = VK\_STRUCTURE\_TYPE\_COMMAND\_BUFFER\_BEGIN\_INFO;
    
    // Record the sorting command.
    vkBeginCommandBuffer(cmdBuffer, &cmdBufferBeginInfo);
    XEG\_HPSRadixSortDescription sortDescription{
        XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION,
        nullptr,
        sortCount,
        keyBuffer,
        indexBuffer
    };
    HMS\_XEG\_CmdRadixSortHPS(cmdBuffer, xegHPS, &sortDescription);
    vkEndCommandBuffer(cmdBuffer);
    
6.  Submit the sorting command.
    
    // Submit the command buffer.
    VkResult res;
    {
        VkSubmitInfo submitInfo{};
        submitInfo.sType = VK\_STRUCTURE\_TYPE\_SUBMIT\_INFO;
        submitInfo.waitSemaphoreCount = 0;
        submitInfo.signalSemaphoreCount = 0;
        submitInfo.pSignalSemaphores = nullptr;
        submitInfo.commandBufferCount = 1;
        submitInfo.pCommandBuffers = &cmdBuffer;
        submitInfo.pWaitSemaphores = nullptr;
        res = vkQueueSubmit(queue, 1, &submitInfo, nullptr);
    }
    // Wait until the operation is complete.
    vkDeviceWaitIdle(device);
    
7.  Destroy an **HPS** object.
    
    if(xegHPS){
        HMS\_XEG\_DestroyHPS(xegHPS);
    }
