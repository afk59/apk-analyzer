# About This Kit

XEngine Kit (GPU acceleration engine service) provides performance enhancement solutions based on Maleoon GPU, including GPU/AI upscaling capabilities, adaptive Variable Rate Shading (VRS), Subpass Shading, ray tracing technologies (including Ray-Traced Reflection, Shadow, Ambient Occlusion, and Global Illumination), and high performance shaders (HPS). Through graphics algorithms and software-hardware optimization, XEngine Kit enables users to enjoy 3D games/apps and AR/VR experiences with higher image quality, better performance, and lower power consumption.

#### Relevant Concepts

Before you get started with development using XEngine Kit, familiarize yourself with the following concepts:

-   [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) is a drawing component typically used to meet developers' complex custom drawing needs, such as displaying camera preview streams and rendering game visuals.
-   Variable Rate Shading (VRS) is a graphics feature allowing apps to control the frequency of pixel shader calling independently of the rendering target's resolution. Adaptive VRS dynamically adjusts the shading rate based on VRS, significantly enhancing the rendering performance.
-   Tile-Based Deferred Rendering (TBDR) is a rendering technology that combines the advantages of Immediate Mode Rendering (IMR) and Deferred Rendering to improve rendering efficiency and reduce memory access.
-   Dynamic Diffuse Global Illumination (DDGI) is a real-time rendering technology, aimed at simulating a global illumination effect obtained after diffuse reflection is performed on light for a plurality of times in a scene, to enhance visual realism.

#### Use Case

## Enhanced Graphics, Lower Power Consumption

When the GPU performance is insufficient to support rendering high-resolution scenes, super-resolution capabilities can be used to enhance user experience by reconstructing lower-resolution images into high-resolution images. Compared to directly rendering high-resolution images, using super-resolution capabilities can reduce the GPU rendering load and decrease power consumption. Currently, the following 3 upscaling capabilities are supported:

-   GPU spatial upscaling: spatial super-sampling based on single-frame images, offering the lowest overhead
-   AI spatial upscaling: GPU/NPU coordinated spatial super-sampling for enhanced results
-   AI temporal upscaling: GPU/NPU coordinated spatial super-sampling for better anti-aliasing performance, higher image quality, and higher upscaling ratio

## Flawless Visuals, Smart Overhead Management

When the GPU performance is limited and cannot provide the same quality level for each pixel of the output image, adaptive VRS can be used to boost the rendering performance. By efficiently allocating computational resources across the image, adaptive VRS reduces rendering frequency without compromising visual quality. This allows different images to be rendered at different rates, effectively improving rendering performance.

## Lower Bandwidth Overhead, Higher Performance

For tile-based deferred rendering (TBDR) and Forward+ pipelines, Subpass Shading can effectively reduce bandwidth overhead and enhance the performance.

## Ray Tracing Acceleration Technology, Efficiently Utilizing the Hardware Ray Tracing Capability

When the GPU supports hardware-based ray tracing, ray tracing rendering technologies can be used to improve the lighting and shadow effects and image quality.

-   **Reflection, Shadow, and Ambient Occlusion**
    
    XEngine Kit provides out-of-the-box ray tracing rendering technologies, including APIs related to Reflection, Shadow, and Ambient Occlusion (AO). Compared with the traditional ray tracing implementation modes, XEngine Kit can achieve higher image quality with a small number of rays, lighter GPU payload for the same image quality, and better image quality under the same payload.
    
-   **Global Illumination**
    
    The XEngine Kit Global Illumination solution, built on hardware ray tracing, AI rendering, and device-cloud rendering, implements real-time global illumination on mobile devices. It employs two technologies: Dynamic Diffuse Global Illumination (DDGI) and Neural Network Global Illumination (NNGI). DDGI is more lightweight and can achieve better power efficiency when working with device-cloud rendering, while NNGI provides better dynamic GI image quality on mobile devices.
    

## High-Performance GPU Sorting

High-performance GPU sorting sorts out-of-order information more quickly, reducing sorting latency and improving performance.

#### Restrictions

-   Before calling XEngine Kit capabilities, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).
-   The following device types are supported: phone, tablet, PC/2-in-1 device, and TV.
-   XEngine Kit features are supported only on devices that use the Maleoon GPU. The supported features vary across devices. You can query the features supported by a device in the following way:
    
    \- For OpenGL ES, use the extension query API [HMS\_XEG\_GetString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_getstring).
    
    \- For Vulkan, use the extension query API [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties).
    
    Both APIs return the supported feature list. For details about how to use the features, please refer to their corresponding sample code.
    

#### Supported Emulators

Currently, this kit does not support emulators.
