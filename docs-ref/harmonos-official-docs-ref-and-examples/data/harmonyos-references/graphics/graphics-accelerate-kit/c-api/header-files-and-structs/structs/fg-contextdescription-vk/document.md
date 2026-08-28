# FG\_ContextDescription\_VK

#### Overview

Describes the attribute information required for creating a frame generation context instance [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7).

**Start version**: 5.0.0(12)

**Related module**: [GraphicsAccelerate](../../../modules/graphicsaccelerate/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

VkInstance [vkInstance](#a8743dce62193ecfaffb7eff178f2a877)

 | 

Vulkan instance, which must be valid throughout the entire lifecycle of [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7).

 |
| 

VkPhysicalDevice [vkPhysicalDevice](#a4237948c43a0da8fbb0bc2278b0027f9)

 | 

Vulkan physical device handle, which must be valid throughout the entire lifecycle of [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7).

 |
| 

VkDevice [vkDevice](#a484ba219df54c20302d07f0aa27129ed)

 | 

Vulkan logical device handle, which must be valid throughout the entire lifecycle of [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7).

 |
| 

uint8\_t [framesInFlight](#a31b5b649ec9ac22013ad2f24b136cc3a)

 | 

Number of frames rendered in parallel. For example, if a frame needs to be rendered after the previous frame is sent for display, **framesInFlight** should be set to **1**. If a frame is being rendered when the previous frame is sent for display, **framesInFlight** should be set to **2**. Note: **framesInFlight** cannot be set to **0**.

Value range: \[1, 2\]

 |
| 

PFN\_vkGetInstanceProcAddr [fnVulkanLoaderFunction](#a83cf228e483f5a26ff0022a3dea788f3)

 | 

Function pointer that points to **vkGetInstanceProcAddr** in Vulkan. The pointer should not be null.

 |

#### Member Variable Description

#### \[h2\]fnVulkanLoaderFunction

PFN\_vkGetInstanceProcAddr FG\_ContextDescription\_VK::fnVulkanLoaderFunction

**Description**

Function pointer that points to **vkGetInstanceProcAddr** in Vulkan. The pointer should not be null.

#### \[h2\]framesInFlight

uint8\_t FG\_ContextDescription\_VK::framesInFlight

**Description**

Number of frames rendered in parallel. For example, if a frame needs to be rendered after the previous frame is sent for display, **framesInFlight** should be set to **1**. If a frame is being rendered when the previous frame is sent for display, **framesInFlight** should be set to **2**. Note: **framesInFlight** cannot be set to **0**.

#### \[h2\]vkDevice

VkDevice FG\_ContextDescription\_VK::vkDevice

**Description**

Vulkan logical device handle, which must be valid throughout the entire lifecycle of [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7).

#### \[h2\]vkInstance

VkInstance FG\_ContextDescription\_VK::vkInstance

**Description**

Vulkan instance, which must be valid throughout the entire lifecycle of [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7).

#### \[h2\]vkPhysicalDevice

VkPhysicalDevice FG\_ContextDescription\_VK::vkPhysicalDevice

**Description**

Vulkan physical device handle, which must be valid throughout the entire lifecycle of [FG\_Context\_VK](../../../modules/graphicsaccelerate/document.md#ga4022ab63c2296d63dcf2c2df178508b7).
