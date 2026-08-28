# Ray-Traced Global Illumination

Since version 6.0.0(20), the Ray-Traced Global Illumination feature is supported.

XEngine Kit provides the on-device Ray-Traced Global Illumination (RTGI) capability, including DDGI and NNGI algorithms.

#### Restrictions

-   Devices need to support Vulkan ray tracing extensions [VK\_KHR\_acceleration\_structure](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_acceleration_structure.html) and [VK\_KHR\_ray\_query](https://docs.vulkan.org/refpages/latest/refpages/source/VK_KHR_ray_query.html).
-   You can check whether the relevant extension is supported as follows:
    
    For Vulkan, use the extension query API [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties). If the query result contains **XEG\_RTGI\_EXTENSION\_NAME**, the extension is supported; otherwise, the extension is not supported.
    

#### Application Scenario

DDGI algorithm: It updates the probe illumination by frame based on the probe information in the viewport to implement real-time rendering of dynamic global illumination using ray tracing. In addition, it can be combined with device-cloud rendering to calculate dynamic global illumination based on the on-device ray tracing power. Based on the static global illumination information sent by the cloud, high-quality global illumination is generated in real time.

NNGI algorithm: It combines AI and ray tracing technologies to perform ray tracing rendering on a scene with a very small resolution (for example, 64 x 32), and then inputs the geometric data and ray tracing result of deferred rendering to the NPU to infer the global illumination result of the entire scene. In this way, the global illumination effect can be achieved with a small number of rays. In addition, based on the heterogeneous collaboration technology of Maleoon GPU, the NPU and GPU can work at the same time, reducing the overall latency.

#### API Description

The following lists APIs for RTGI setting. For details about more setting and query APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine).

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, XEG\_ExtensionProperties \*pProperties)

 | 

Queries XEngine Vulkan extensions.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateRTGI (VkDevice device, const void \*pCreateInfo, XEG\_RTGI \*pRtGI)

 | 

Creates an **XEG\_RTGI** object.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdRenderRTGI (VkCommandBuffer commandBuffer, XEG\_RTGI rtGI, const void \*pDescription)

 | 

Executes the rendering command.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CmdSetSynchronization (VkCommandBuffer commandBuffer, const void \*xegHandle)

 | 

Sets the synchronization signal and waits for the rendering result to be written to a specified image. When the RTGI feature is used, it is the GI rendering result that needs to be waited for before being written to a specified image.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyRTGI (XEG\_RTGI rtGI)

 | 

Destroys an **XEG\_RTGI** object.

 |

#### DDGI Development Procedure

This section uses integrating the Vulkan graphics APIs as an example to describe the XEngine integration process.

## Configuring Your Project

When compiling the HAP, add build dependency **libxengine.so** in the NDK for the .so files at the Native layer.

-   Referencing the header files
    
    #include <algorithm>
    #include <string>
    #include <vector>
    #include <xengine/xeg\_vulkan\_rtgi.h>
    #include <xengine/xeg\_vulkan\_extension.h>
    #include <xengine/xeg\_extension\_defs.h>
    
-   Compiling CMakeLists.txt
    
    The following shows part of the sample code in **CMakeLists.txt**.
    
    find\_library(
        # Set the name of the path variable.
        xengine-lib
        # Specify the name of the NDK library that you want CMake to locate.
        xengine
    )
    target\_link\_libraries(ohosmain PUBLIC
        ...... // Other library files.
        ${xengine-lib} RenderBehavior SceneLoader VulkanBase
    )
    

## Integrating XEngine RT DDGI (Vulkan)

Set up the image rendering pipeline using Vulkan graphics APIs, and integrate RT DDGI at the Native layer. The rendering results are displayed on the screen through [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).

This section describes how to use RT DDGI by calling Vulkan graphics APIs.

Before calling XEngine Kit capabilities, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties) to obtain the extensions supported by XEngine. The RT DDGI APIs can be used only when the **XEG\_RTGI\_EXTENSION\_NAME** extension is supported.
    
    // **physicalDevice** indicates a physical device defined by Vulkan and needs to be initialized.
    VkPhysicalDevice physicalDevice;
    // Query the Vulkan extensions supported by XEngine.
    std::vector<std::string> supportedExtensions;
    uint32\_t propertyCount;
    HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, nullptr);
    if (propertyCount> 0) {
        std::vector<XEG\_ExtensionProperties> properties(propertyCount);
        if (HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount,
            &properties.front()) == VK\_SUCCESS) {
            for (auto ext : properties) {
                supportedExtensions.push\_back(ext.extensionName);
            }
        }
    }
    // Check whether RT DDGI is supported.
    if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG\_RTGI\_EXTENSION\_NAME) ==
        supportedExtensions.end()) {
        exit(1);
    }
    
2.  Declare the instance handle.
    
    XEG\_RTGI xegRTGI;
    
3.  Call [HMS\_XEG\_CreateRTGI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_creatertgi) to create an RT DDGI instance.
    
    // The rendering width, height, and scaling ratio can be set by the user. The following uses 1280 x 720 as an example, and the scaling ratio is 1.
    VkExtent2D outputSize;
    outputSize.width = 1280;
    outputSize.height = 720;
    VkExtent2D scaled;
    scaled.width = 1;
    scaled.height = 1;
    // Logical device defined by Vulkan, which needs to be initialized.
    VkDevice device;
    // **XEG\_DDGICreateInfo** indicates the information required for creating an **XEG\_RTGI** object.
    struct XEG\_DDGICreateInfo DDGICreateInfo;
    // Specify the current structure type as **create info**.
    DDGICreateInfo.sType = XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO;
    // Specify no extension.
    DDGICreateInfo.pNext = nullptr;
    // Specify the quality mode as Balanced mode.
    DDGICreateInfo.qualityMode = XEG\_RTGI\_QUALITY\_MODE\_BALANCED;
    // Specify the maximum number of volumes that need to be rendered at the same time in the current scene. The value range is \[1, 9\].
    DDGICreateInfo.numberVolume = 4;
    // Specify the scaling ratio of the rendering width and height. The recommended value range is \[1, 4\]. The value must be greater than or equal to 1.
    DDGICreateInfo.scaledView = scaled;
    // Specify the rendering width and height of output GI images.
    DDGICreateInfo.viewSize = outputSize;
    // Specify whether to enable the device-cloud mode (**true**) or not (**false**).
    DDGICreateInfo.enableCloud = false;
    VkResult res = HMS\_XEG\_CreateRTGI(device, &DDGICreateInfo, &xegRTGI);
    if (res != VK\_SUCCESS) {
        exit(1);
    }
    
4.  Call [HMS\_XEG\_CmdRenderRTGI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdrenderrtgi) to execute the rendering command for each frame.
    
    // **probeIrradianceSH** indicates the **VkImageView** of the 3D image for storing the second-order spherical harmonic coefficients of the probe irradiance. You need to create this **VkImageView**.
    // Store the rendering result of the current API. The GI illumination value can be calculated by sampling the image using trilinear interpolation.
    VkImageView probeIrradianceSH = VK\_NULL\_HANDLE;
    // Define a **DDGIVolumeEntryParameters** object for **XEG\_DDGIVolumeEntryParameters**.
    struct XEG\_DDGIVolumeEntryParameters DDGIVolumeEntryParameters;
    // Volume index, which is unique. The value range is \[0, 65535\].
    DDGIVolumeEntryParameters.volumeIndex = 0;
    // Number of rays emitted by probes. The value range is \[1, 1024\].
    DDGIVolumeEntryParameters.raysPerProbe = 128;
    // Calculate the maximum distance of ray intersection.
    DDGIVolumeEntryParameters.probeMaxRayDistance = 1000.0f;
    // Coordinates of the volume center point.
    DDGIVolumeEntryParameters.volumePosition\[0\] = 0.0f;
    DDGIVolumeEntryParameters.volumePosition\[1\] = 0.0f;
    DDGIVolumeEntryParameters.volumePosition\[2\] = 0.0f;
    // Probe spacing. The value must be greater than 0.
    DDGIVolumeEntryParameters.probeSpacing\[0\] = 10.0f;
    DDGIVolumeEntryParameters.probeSpacing\[1\] = 10.0f;
    DDGIVolumeEntryParameters.probeSpacing\[2\] = 10.0f;
    // Volume lighting channel mask.
    DDGIVolumeEntryParameters.volumeLightingChannelMask = 0xFFFFFFFF;
    // Number of probes. The value must be greater than 0. The value range is \[1, 32\].
    DDGIVolumeEntryParameters.volumeProbeGridCounts\[0\] = 6;
    DDGIVolumeEntryParameters.volumeProbeGridCounts\[1\] = 6;
    DDGIVolumeEntryParameters.volumeProbeGridCounts\[2\] = 6;
    // Gamma correction coefficient of light. The value cannot be 0.
    DDGIVolumeEntryParameters.volumeProbeIrradianceEncodingGamma = 5.0f;
    // Historical weight of probe light. The value range is \[0, 1\].
    DDGIVolumeEntryParameters.probeHysteresis = 0.95f;
    // Probe change threshold.
    DDGIVolumeEntryParameters.probeChangeThreshold = 1.0f;
    // Probe brightness threshold.
    DDGIVolumeEntryParameters.probeBrightnessThreshold = 1.0f;
    // Probe normal bias.
    DDGIVolumeEntryParameters.volumeNormalBias = 0.12f;
    // Probe view bias.
    DDGIVolumeEntryParameters.volumeViewBias = 0.48f;
    // Volume lighting blending distance.
    DDGIVolumeEntryParameters.volumeBlendDistance = 1.0;
    // Fade-in range of the lighting at the volume edges.
    DDGIVolumeEntryParameters.volumeBlendDistanceBlack = 1.0;
    // Backward judgment threshold of probes.
    DDGIVolumeEntryParameters.probeBackfaceThreshold = 1.0;
    // Minimum forward distance of probes.
    DDGIVolumeEntryParameters.probeMinFrontfaceDistance = 1.0;
    // Volume irradiance scaling ratio. The value must be non-negative.
    DDGIVolumeEntryParameters.volumeIrradianceScalar = 1.0;
    // Emissive intensity multiplier. The value must be non-negative.
    DDGIVolumeEntryParameters.emissiveMultiplier = 1.0;
    // Lighting multiplier. The value must be non-negative.
    DDGIVolumeEntryParameters.lightingMultiplier = 1.0;
    // Whether to forcibly update all probes. The value **true** indicates that all probes are forcibly updated, and the value **false** indicates that some probes are updated.
    DDGIVolumeEntryParameters.bForceUpdate = false;
    DDGIVolumeEntryParameters.probeIrradianceSH = probeIrradianceSH;
    
    // Define a **DDGIDescription** object for **XEG\_DDGIDescription**.
    struct XEG\_DDGIDescription DDGIDescription;
    // **inputNormalImage** indicates the **VkImageView** of the normal map. You need to create this **VkImageView**.
    VkImageView inputNormalImage = VK\_NULL\_HANDLE;
    // **inputDepthImage** indicates the **VkImageView** of the depth image. You need to create this **VkImageView**.
    VkImageView inputDepthImage = VK\_NULL\_HANDLE;
    // **inputBasecolorMetallicImage** indicates the **VkImageView** of the color and metallic image. You need to create this **VkImageView**.
    VkImageView inputBasecolorMetallicImage = VK\_NULL\_HANDLE;
    // **inputDirectionImage** indicates the **VkImageView** of the emission direction image. You need to create this **VkImageView**.
    VkImageView inputDirectionImage = VK\_NULL\_HANDLE;
    // **inputRayRadianceDistanceImage** indicates the **VkImageView** of the ray intersection radiance and distance image. You need to create this **VkImageView**.
    VkImageView inputRayRadianceDistanceImage = VK\_NULL\_HANDLE;
    // **inputRayHitNormalAndMetallicImage** indicates the **VkImageView** of the ray intersection normal and metallic image. You need to create this **VkImageView**.
    VkImageView inputRayHitNormalAndMetallicImage = VK\_NULL\_HANDLE;
    // **inputVolumeIndexAndProbeIndex** indicates the **VkBuffer** of the input probe index buffer. You need to create this **VkBuffer**.
    VkBuffer inputVolumeIndexAndProbeIndex = VK\_NULL\_HANDLE;
    // **outputVolumeIndexAndProbeIndex** indicates the **VkBuffer** of the output probe index buffer. You need to create this **VkBuffer**.
    VkBuffer outputVolumeIndexAndProbeIndex = VK\_NULL\_HANDLE;
    // **outputProbeCount** indicates the **VkBuffer** of the output probe count buffer. You need to create this **VkBuffer**.
    VkBuffer outputProbeCount = VK\_NULL\_HANDLE;
    // **outputGIImage** indicates the **VkImageView** of the global illumination image. You need to create this **VkImageView**.
    VkImageView outputGIImage = VK\_NULL\_HANDLE;
    // **commandBuffer** indicates the command buffer and needs to be initialized.
    VkCommandBuffer commandBuffer = VK\_NULL\_HANDLE;
    // Specify the current structure type as **DDGI description**.
    DDGIDescription.sType = XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION;
    // Specify no extension.
    DDGIDescription.pNext = nullptr;
    // Set the camera-related matrix.
    for (uint32\_t i = 0; i < 16; ++i) {
        DDGIDescription.viewMatrix\[i\] = 1.0f;
        DDGIDescription.projectionMatrix\[i\] = 1.0f;
    }
    DDGIDescription.inputNormalImage = inputNormalImage;
    DDGIDescription.inputDepthImage = inputDepthImage;
    DDGIDescription.inputBasecolorMetallicImage = inputBasecolorMetallicImage;
    DDGIDescription.inputDirectionImage = inputDirectionImage;
    DDGIDescription.inputRayRadianceDistanceImage = inputRayRadianceDistanceImage;
    DDGIDescription.inputRayHitNormalAndMetallicImage = inputRayHitNormalAndMetallicImage;
    DDGIDescription.inputVolumeIndexAndProbeIndex = inputVolumeIndexAndProbeIndex;
    // Input the number of probes.
    DDGIDescription.inputProbeCount = 10;
    DDGIDescription.outputVolumeIndexAndProbeIndex = outputVolumeIndexAndProbeIndex;
    DDGIDescription.outputProbeCount = outputProbeCount;
    DDGIDescription.outputGIImage = outputGIImage;
    // Number of used volumes.
    DDGIDescription.enableVolumeNumber = 1;
    DDGIDescription.pVolumeEntryParameters = &DDGIVolumeEntryParameters;
    HMS\_XEG\_CmdRenderRTGI(commandBuffer, xegRTGI, &DDGIDescription);
    
5.  If the deferred rendering pipeline is used, call [HMS\_XEG\_CmdRenderRTGI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdrenderrtgi). Then call [HMS\_XEG\_CmdSetSynchronization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdsetsynchronization) to set the synchronization signal and wait for the GI rendering result to be written to the specified image. The [HMS\_XEG\_CmdSetSynchronization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdsetsynchronization) API must be called for each frame.
    
    // The GI rendering result is written to the **outputGIImage** image in **XEG\_DDGIDescription**.
    HMS\_XEG\_CmdSetSynchronization(commandBuffer, &xegRTGI);
    
6.  Call [HMS\_XEG\_DestroyRTGI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_destroyrtgi) to destroy the instance.
    
    if (xegRTGI) {
        HMS\_XEG\_DestroyRTGI(xegRTGI);
    }
    

#### NNGI Development Procedure

This section uses integrating the Vulkan graphics APIs as an example to describe the XEngine integration process.

## Configuring Your Project

When compiling the HAP, add build dependency **libxengine.so** in the NDK for the .so files at the Native layer.

-   Referencing the header files
    
    #include <algorithm>
    #include <string>
    #include <vector>
    #include "xengine/xeg\_vulkan\_rtgi.h"
    #include "xengine/xeg\_vulkan\_extension.h"
    
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
    

## Integrating XEngine RT NNGI (Vulkan)

Set up the image rendering pipeline using Vulkan graphics APIs, and integrate RT NNGI at the Native layer. The rendering results are displayed on the screen through [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).

This section describes how to use RT NNGI by calling Vulkan graphics APIs.

Before calling XEngine Kit capabilities, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties) to obtain the extensions supported by XEngine. The RT NNGI APIs can be used only when the **XEG\_RTGI\_EXTENSION\_NAME** extension is supported.
    
    // **physicalDevice** indicates a physical device defined by Vulkan and needs to be initialized.
    VkPhysicalDevice physicalDevice;
    // Query the Vulkan extensions supported by XEngine.
    std::vector<std::string> supportedExtensions;
    uint32\_t propertyCount;
    HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount, nullptr);
    if (propertyCount> 0) {
        std::vector<XEG\_ExtensionProperties> properties(propertyCount);
        if (HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &propertyCount,
            &properties.front()) == VK\_SUCCESS) {
            for (auto ext : properties) {
                supportedExtensions.push\_back(ext.extensionName);
            }
        }
    }
    // Check whether RT NNGI is supported.
    if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG\_RTGI\_EXTENSION\_NAME) ==
        supportedExtensions.end()) {
        exit(1);
    }
    
2.  Declare the instance handle.
    
    XEG\_RTGI xegRTGI;
    
3.  Call [HMS\_XEG\_CreateRTGI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_creatertgi) to create an RT NNGI instance.
    
    // Logical device defined by Vulkan, which needs to be initialized.
    VkDevice device;
    // **XEG\_DDGICreateInfo** indicates the information required for creating an **XEG\_RTGI** object.
    XEG\_NNGICreateInfo NNGICreateInfo;
    // Specify the current structure type as **create info**.
    NNGICreateInfo.sType = XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO;
    // Specify no extension.
    NNGICreateInfo.pNext = nullptr;
    // Specify the quality mode as Balanced mode.
    NNGICreateInfo.qualityMode = XEG\_RTGI\_QUALITY\_MODE\_BALANCED;
    // Specify the resolution of the inference input image.
    NNGICreateInfo.inferenceInputSize = {1280,720};
    // Specify the resolution of the inference output image. Currently, only (640, 328) is supported.
    NNGICreateInfo.inferenceOutputSize = {640, 368};
    // Specify the resolution of the training image.
    NNGICreateInfo.trainingSize = {64, 32};
    VkResult res = HMS\_XEG\_CreateRTGI(device, &NNGICreateInfo, &xegRTGI);
    if (res != VK\_SUCCESS) {
        exit(1);
    }
    
4.  Call [HMS\_XEG\_CmdRenderRTGI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdrenderrtgi) to execute the rendering command for each frame.
    
    // Define an **NNGIDescription** object for **XEG\_NNGIDescription**.
    struct XEG\_NNGIDescription NNGIDescription;
    // **inferenceInputDepthImage** indicates the **VkImageView** of the inference input depth image. You need to create this **VkImageView**.
    VkImageView inferenceInputDepthImage = VK\_NULL\_HANDLE;
    // **inferenceInputNormalImage** indicates the **VkImageView** of the inference input normal vector image. You need to create this **VkImageView**.
    VkImageView inferenceInputNormalImage = VK\_NULL\_HANDLE;
    // **inferenceInputBaseColorMetallicImage** indicates the **VkImageView** of the inference input base color and metallic image. You need to create this **VkImageView**.
    VkImageView inferenceInputBaseColorMetallicImage = VK\_NULL\_HANDLE;
    // **inferenceOutputGIImage** indicates the **VkImageView** of the inference output global illumination image. You need to create this **VkImageView**.
    VkImageView inferenceOutputGIImage = VK\_NULL\_HANDLE;
    // **trainingInputPositionImage** indicates the **VkImageView** of the training input position image. You need to create this **VkImageView**.
    VkImageView trainingInputPositionImage = VK\_NULL\_HANDLE;
    // **trainingInputNormalImage** indicates the **VkImageView** of the training input normal vector image. You need to create this **VkImageView**.
    VkImageView trainingInputNormalImage = VK\_NULL\_HANDLE;
    // **trainingInputBaseColorMetallicImage** indicates the **VkImageView** of the training input base color and metallic image. You need to create this **VkImageView**.
    VkImageView trainingInputBaseColorMetallicImage = VK\_NULL\_HANDLE;
    // **trainingInputGIImage** indicates the **VkImageView** of the training input global illumination image. You need to create this **VkImageView**.
    VkImageView trainingInputGIImage = VK\_NULL\_HANDLE;
    // **sceneAabb** indicates the **VkAabbPositionsKHR** of the rendering bounding box range. You need to create this **VkAabbPositionsKHR**.
    VkAabbPositionsKHR sceneAabb = {0,0,0,1,1,1};
    // **isSceneUnbounded** specifies whether the rendering scene is unbounded. Currently, only **false** is supported.
    bool isSceneUnbounded = false;
    // **spatialScaleFactor** indicates the scene scaling factor. For bounded scenes, this parameter does not need to be set. XEngine calculates the value based on **sceneAabb**.
    float spatialScaleFactor = 0;
    // **commandBuffer** indicates the command buffer and needs to be initialized.
    VkCommandBuffer commandBuffer = VK\_NULL\_HANDLE;
    // Specify the current structure type as **DDGI description**.
    NNGIDescription.sType = XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION;
    // Specify no extension.
    NNGIDescription.pNext = nullptr;
    // Set camera matrices for inference images. You need to initialize them for actual use. The following are examples only.
    float inferenceCameraViewMatrix\[16\];
    float inferenceCameraProjectionMatrix\[16\];
    memcpy(NNGIDescription.inferenceCameraViewMatrix, &inferenceCameraViewMatrix, sizeof(NNGIDescription.inferenceCameraViewMatrix));
    memcpy(NNGIDescription.inferenceCameraProjectionMatrix, &inferenceCameraProjectionMatrix, sizeof(NNGIDescription.inferenceCameraProjectionMatrix));
    // Set camera matrices for training images. You need to initialize them for actual use. The following are examples only.
    float trainingCameraViewMatrix\[16\];
    float trainingCameraProjectionMatrix\[16\];
    memcpy(NNGIDescription.trainingCameraViewMatrix, &trainingCameraViewMatrix, sizeof(NNGIDescription.trainingCameraViewMatrix));
    memcpy(NNGIDescription.trainingCameraProjectionMatrix, &trainingCameraProjectionMatrix, sizeof(NNGIDescription.trainingCameraProjectionMatrix)); 
    NNGIDescription.inferenceInputDepthImage = inferenceInputDepthImage;
    NNGIDescription.inferenceInputNormalImage = inferenceInputNormalImage;
    NNGIDescription.inferenceInputBaseColorMetallicImage = inferenceInputBaseColorMetallicImage;
    NNGIDescription.inferenceOutputGIImage = inferenceOutputGIImage;
    NNGIDescription.trainingInputPositionImage = trainingInputPositionImage;
    NNGIDescription.trainingInputNormalImage = trainingInputNormalImage;
    NNGIDescription.trainingInputBaseColorMetallicImage = trainingInputBaseColorMetallicImage;
    NNGIDescription.trainingInputGIImage = trainingInputGIImage;
    NNGIDescription.sceneAabb = sceneAabb;
    NNGIDescription.isSceneUnbounded = isSceneUnbounded;
    NNGIDescription.spatialScaleFactor = spatialScaleFactor;
    HMS\_XEG\_CmdRenderRTGI(commandBuffer, xegRTGI, &NNGIDescription);
    
5.  Call [HMS\_XEG\_CmdRenderRTGI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdrenderrtgi). Then call [HMS\_XEG\_CmdSetSynchronization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdsetsynchronization) to execute the training step. The [HMS\_XEG\_CmdSetSynchronization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdsetsynchronization) API must be called for each frame.
    
    // The GI rendering result is written to the **inferenceOutputGIImage** image in **XEG\_NNGIDescription**.
    HMS\_XEG\_CmdSetSynchronization(commandBuffer, &xegRTGI);
    
6.  Call [HMS\_XEG\_DestroyRTGI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_destroyrtgi) to destroy the instance.
    
    if (xegRTGI) {
        HMS\_XEG\_DestroyRTGI(xegRTGI);
    }
