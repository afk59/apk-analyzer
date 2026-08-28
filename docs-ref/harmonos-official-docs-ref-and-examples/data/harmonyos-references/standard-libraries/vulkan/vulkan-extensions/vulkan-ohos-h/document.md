# vulkan\_ohos.h

#### Overview

The file declares the Vulkan interfaces extended by HarmonyOS.

**File to include**: <vulkan/vulkan\_ohos.h>

**Library**: libvulkan.so

**Since**: 10

**Related module**: [Vulkan](../vulkan/document.md)

#### Summary

## Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [VkSurfaceCreateInfoOHOS](../vksurfacecreateinfoohos/document.md) | VkSurfaceCreateInfoOHOS | Describes the parameters required for creating a Vulkan surface. |
| [VkNativeBufferOHOS](../vknativebufferohos/document.md) | VkNativeBufferOHOS | Contains parameters for the native device memory. |
| [VkSwapchainImageCreateInfoOHOS](../vkswapchainimagecreateinfoohos/document.md) | VkSwapchainImageCreateInfoOHOS | Contains parameters required for creating an image. |
| [VkPhysicalDevicePresentationPropertiesOHOS](../vkphysicaldevicepresentationpropertiesohos/document.md) | VkPhysicalDevicePresentationPropertiesOHOS | Contains parameters for the display attributes of the device. |
| [VkNativeBufferUsageOHOS](../vknativebufferusageohos/document.md) | VkNativeBufferUsageOHOS | Describes the usage of the NativeBuffer. |
| [VkNativeBufferPropertiesOHOS](../vknativebufferpropertiesohos/document.md) | VkNativeBufferPropertiesOHOS | Describes the properties of the NativeBuffer. |
| [VkNativeBufferFormatPropertiesOHOS](../vknativebufferformatpropertiesohos/document.md) | VkNativeBufferFormatPropertiesOHOS | Describes the format properties of the NativeBuffer. |
| [VkImportNativeBufferInfoOHOS](../vkimportnativebufferinfoohos/document.md) | VkImportNativeBufferInfoOHOS | Describes the pointer to an OH\_NativeBuffer struct. |
| [VkMemoryGetNativeBufferInfoOHOS](../vkmemorygetnativebufferinfoohos/document.md) | VkMemoryGetNativeBufferInfoOHOS | Used to obtain an OH\_NativeBuffer from the Vulkan memory. |
| [VkExternalFormatOHOS](../vkexternalformatohos/document.md) | VkExternalFormatOHOS | Describes an externally defined format. |
| [NativeWindow](../nativewindow/document.md) | OHNativeWindow | Describes a native window. |
| [OHBufferHandle](../ohbufferhandle/document.md) | \- | Describes the buffer handle, which is used to transfer and obtain buffer information. |
| [OH\_NativeBuffer](../oh-nativebuffer/document.md) | \- | Describes the OH\_NativeBuffer struct. |

## Enumeration

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [VkSwapchainImageUsageFlagBitsOHOS](#vkswapchainimageusageflagbitsohos) | VkSwapchainImageUsageFlagBitsOHOS | Image usage flag. |

## Macros

| Name | Description |
| :-- | :-- |
| VK\_OHOS\_surface 1 | 
Surface extension macro definition of HarmonyOS.

**Since**: 10

 |
| VK\_OHOS\_SURFACE\_SPEC\_VERSION 1 | 

Surface extension version of HarmonyOS.

**Since**: 10

 |
| VK\_OHOS\_SURFACE\_EXTENSION\_NAME "VK\_OHOS\_surface" | 

Surface extension name of HarmonyOS.

**Since**: 10

 |
| VK\_OHOS\_native\_buffer 1 | 

Extended macro definition for native\_buffer.

**Since**: 10

 |
| VK\_OHOS\_NATIVE\_BUFFER\_SPEC\_VERSION 1 | 

Extended version number for native\_buffer.

**Since**: 10

 |
| VK\_OHOS\_NATIVE\_BUFFER\_EXTENSION\_NAME "VK\_OHOS\_native\_buffer" | 

native\_buffer extension name.

**Since**: 10

 |
| VK\_OHOS\_external\_memory 1 | 

External memory extension macro definition of HarmonyOS.

**Since**: 10

 |
| VK\_OHOS\_EXTERNAL\_MEMORY\_SPEC\_VERSION 1 | 

External memory extension version of HarmonyOS.

**Since**: 10

 |
| VK\_OHOS\_EXTERNAL\_MEMORY\_EXTENSION\_NAME "VK\_OHOS\_external\_memory" | 

External memory extension name of HarmonyOS.

**Since**: 10

 |

## Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [VkResult (VKAPI\_PTR PFN\_vkCreateSurfaceOHOS)(VkInstance instance, const VkSurfaceCreateInfoOHOS pCreateInfo, const VkAllocationCallbacks\* pAllocator, VkSurfaceKHR\* pSurface)](#pfn_vkcreatesurfaceohos) | PFN\_vkCreateSurfaceOHOS | Defines the function pointer for creating a Vulkan surface. |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkCreateSurfaceOHOS(VkInstance instance, const VkSurfaceCreateInfoOHOS\* pCreateInfo, const VkAllocationCallbacks\* pAllocator, VkSurfaceKHR\* pSurface)](#vkcreatesurfaceohos) | \- | Creates a Vulkan surface. |
| [VkResult (VKAPI\_PTR PFN\_vkGetNativeBufferPropertiesOHOS)(VkDevice device, const struct OH\_NativeBuffer buffer, VkNativeBufferPropertiesOHOS\* pProperties)](#pfn_vkgetnativebufferpropertiesohos) | PFN\_vkGetNativeBufferPropertiesOHOS | Defines a function pointer used to obtain OH\_NativeBuffer properties. |
| [VkResult (VKAPI\_PTR PFN\_vkGetMemoryNativeBufferOHOS)(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS pInfo, struct OH\_NativeBuffer\*\* pBuffer)](#pfn_vkgetmemorynativebufferohos) | PFN\_vkGetMemoryNativeBufferOHOS | Defines a function pointer used to obtain an OH\_NativeBuffer instance. |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkGetNativeBufferPropertiesOHOS(VkDevice device, const struct OH\_NativeBuffer\* buffer, VkNativeBufferPropertiesOHOS\* pProperties)](#vkgetnativebufferpropertiesohos) | \- | Obtains the properties of an OH\_NativeBuffer instance. |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkGetMemoryNativeBufferOHOS(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS\* pInfo, struct OH\_NativeBuffer\*\* pBuffer)](#vkgetmemorynativebufferohos) | \- | Obtains an OH\_NativeBuffer instance. |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkGetSwapchainGrallocUsageOHOS(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64\_t\* grallocUsage)](#vkgetswapchaingrallocusageohos) | \- | Returns the appropriate gralloc usage flag based on the given Vulkan device, image format, and image usage flag. |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkAcquireImageOHOS(VkDevice device, VkImage image, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)](#vkacquireimageohos) | \- | Obtains the ownership of the swap chain image and imports the fence of the external signal to the VkSemaphore and VkFence objects. |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkQueueSignalReleaseImageOHOS(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore\* pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)](#vkqueuesignalreleaseimageohos) | \- | Sends a signal to the system hardware buffer to release an image once it is no longer needed so that other components can access it. |
| [VkResult (VKAPI\_PTR \*PFN\_vkSetNativeFenceFdOpenHarmony)(VkDevice device, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)](#vkapi_ptr-pfn_vksetnativefencefdopenharmony) | VKAPI\_PTR \*PFN\_vkSetNativeFenceFdOpenHarmony | This API has been deprecated. |
| [typedef VkResult (VKAPI\_PTR PFN\_vkGetNativeFenceFdOpenHarmony)(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)](#vkapi_ptr-pfn_vkgetnativefencefdopenharmony) | VKAPI\_PTR \*PFN\_vkGetNativeFenceFdOpenHarmony | This API has been deprecated. |
| [VkResult (VKAPI\_PTR PFN\_vkGetSwapchainGrallocUsageOHOS)(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64\_t grallocUsage)](#vkapi_ptr-pfn_vkgetswapchaingrallocusageohos) | VKAPI\_PTR \*PFN\_vkGetSwapchainGrallocUsageOHOS | Returns the appropriate gralloc usage flag based on the given Vulkan device, image format, and image usage flag. As an application developer, you do not need to use this function. |
| [VkResult (VKAPI\_PTR \*PFN\_vkAcquireImageOHOS)(VkDevice device, VkImage image, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)](#vkapi_ptr-pfn_vkacquireimageohos) | VKAPI\_PTR \*PFN\_vkAcquireImageOHOS | Obtains the ownership of the swap chain image and imports the fence of the external signal to the VkSemaphore and VkFence objects. As an application developer, you do not need to use this function. |
| [typedef VkResult (VKAPI\_PTR PFN\_vkQueueSignalReleaseImageOHOS)(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)](#vkapi_ptr-pfn_vkqueuesignalreleaseimageohos) | VKAPI\_PTR \*PFN\_vkQueueSignalReleaseImageOHOS | Sends a signal to the system hardware buffer to release an image once it is no longer needed so that other components can access it. As an application developer, you do not need to use this function. |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkSetNativeFenceFdOpenHarmony(VkDevice device, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)](#vksetnativefencefdopenharmony) | \- | This API has been deprecated. |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkGetNativeFenceFdOpenHarmony(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore\* pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)](#vkgetnativefencefdopenharmony) | \- | This API has been deprecated. |

#### Enumeration Description

## VkSwapchainImageUsageFlagBitsOHOS

enum VkSwapchainImageUsageFlagBitsOHOS

**Description**

Image usage flag.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| VK\_SWAPCHAIN\_IMAGE\_USAGE\_SHARED\_BIT\_OHOS = 0x00000001 | Shared image flag. |
| VK\_SWAPCHAIN\_IMAGE\_USAGE\_FLAG\_BITS\_MAX\_ENUM\_OHOS = 0x7FFFFFFF | Maximum value. |

#### Function Description

#### \[h2\]PFN\_vkCreateSurfaceOHOS()

typedef VkResult (VKAPI\_PTR \*PFN\_vkCreateSurfaceOHOS)(VkInstance instance, const VkSurfaceCreateInfoOHOS\* pCreateInfo, const VkAllocationCallbacks\* pAllocator, VkSurfaceKHR\* pSurface)

**Description**

Defines the function pointer for creating a Vulkan surface.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| VkInstance instance | Vulkan instance. |
| [const VkSurfaceCreateInfoOHOS](../vksurfacecreateinfoohos/document.md)\* pCreateInfo | Pointer to the VkSurfaceCreateInfoOHOS struct, including the parameters required for creating a Vulkan surface. |
| const VkAllocationCallbacks\* pAllocator | Pointer to a callback function for custom memory allocation. If custom memory allocation is not required, pass in NULL, and the default memory allocation function is used. |
| VkSurfaceKHR\* pSurface | Pointer to the Vulkan surface created. The type is **VkSurfaceKHR**. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | **VK\_SUCCESS**. If the operation fails, an error code of the VkResult type is returned. |

#### \[h2\]vkCreateSurfaceOHOS()

VKAPI\_ATTR VkResult VKAPI\_CALL vkCreateSurfaceOHOS(VkInstance instance, const VkSurfaceCreateInfoOHOS\* pCreateInfo, const VkAllocationCallbacks\* pAllocator, VkSurfaceKHR\* pSurface)

**Description**

Creates a Vulkan surface.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| VkInstance instance | Vulkan instance. |
| [const VkSurfaceCreateInfoOHOS](../vksurfacecreateinfoohos/document.md)\* pCreateInfo | Pointer to the VkSurfaceCreateInfoOHOS struct, including the parameters required for creating a Vulkan surface. |
| const VkAllocationCallbacks\* pAllocator | Pointer to a callback function for custom memory allocation. If custom memory allocation is not required, pass in NULL, and the default memory allocation function is used. |
| VkSurfaceKHR\* pSurface | Pointer to the Vulkan surface created. The type is **VkSurfaceKHR**. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | 
One of the following error codes of the VkResult type:

**VK\_SUCCESS**: The operation is successful.

**VK\_ERROR\_OUT\_OF\_HOST\_MEMORY**: The VkSurfaceKHR memory fails to be allocated.

**VK\_ERROR\_SURFACE\_LOST\_KHR**: The NativeWindow operation fails.

 |

#### \[h2\]PFN\_vkGetNativeBufferPropertiesOHOS()

typedef VkResult (VKAPI\_PTR \*PFN\_vkGetNativeBufferPropertiesOHOS)(VkDevice device, const struct OH\_NativeBuffer\* buffer, VkNativeBufferPropertiesOHOS\* pProperties)

**Description**

Defines a function pointer used to obtain OH\_NativeBuffer properties.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| VkDevice device | VkDevice object. |
| const [struct OH\_NativeBuffer](../oh-nativebuffer/document.md)\* buffer | Pointer to an OH\_NativeBuffer struct. |
| [VkNativeBufferPropertiesOHOS](../vknativebufferpropertiesohos/document.md)\* pProperties | Pointer to the struct holding the properties of OH\_NativeBuffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | **VK\_SUCCESS**. If the operation fails, an error code of the VkResult type is returned. |

#### \[h2\]PFN\_vkGetMemoryNativeBufferOHOS()

typedef VkResult (VKAPI\_PTR \*PFN\_vkGetMemoryNativeBufferOHOS)(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS\* pInfo, struct OH\_NativeBuffer\*\* pBuffer)

**Description**

Defines a function pointer used to obtain an OH\_NativeBuffer instance.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| VkDevice device | VkDevice object. |
| [const VkMemoryGetNativeBufferInfoOHOS](../vkmemorygetnativebufferinfoohos/document.md)\* pInfo | Pointer to a VkMemoryGetNativeBufferInfoOHOS struct. |
| [struct OH\_NativeBuffer](../oh-nativebuffer/document.md)\*\* pBuffer | Pointer to the OH\_NativeBuffer obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | **VK\_SUCCESS**. If the operation fails, an error code of the VkResult type is returned. |

#### \[h2\]vkGetNativeBufferPropertiesOHOS()

VKAPI\_ATTR VkResult VKAPI\_CALL vkGetNativeBufferPropertiesOHOS(VkDevice device, const struct OH\_NativeBuffer\* buffer, VkNativeBufferPropertiesOHOS\* pProperties)

**Description**

Obtains the properties of an OH\_NativeBuffer instance.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| VkDevice device | VkDevice object. |
| const [struct OH\_NativeBuffer](../oh-nativebuffer/document.md)\* buffer | Pointer to an OH\_NativeBuffer struct. |
| [VkNativeBufferPropertiesOHOS](../vknativebufferpropertiesohos/document.md)\* pProperties | Pointer to the struct holding the properties of OH\_NativeBuffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | 
One of the following error codes of the VkResult type:

**VK\_SUCCESS**: The operation is successful.

**VK\_ERROR\_INVALID\_EXTERNAL\_HANDLE\_KHR**: An input parameter is abnormal.

**VK\_ERROR\_OUT\_OF\_DEVICE\_MEMORY**: The device memory is insufficient.

 |

#### \[h2\]vkGetMemoryNativeBufferOHOS()

VKAPI\_ATTR VkResult VKAPI\_CALL vkGetMemoryNativeBufferOHOS(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS\* pInfo, struct OH\_NativeBuffer\*\* pBuffer)

**Description**

Obtains an OH\_NativeBuffer instance.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| VkDevice device | VkDevice object. |
| [const VkMemoryGetNativeBufferInfoOHOS](../vkmemorygetnativebufferinfoohos/document.md)\* pInfo | Pointer to a VkMemoryGetNativeBufferInfoOHOS struct. |
| [struct OH\_NativeBuffer](../oh-nativebuffer/document.md)\*\* pBuffer | Pointer to the OH\_NativeBuffer obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | 
One of the following error codes of the VkResult type:

**VK\_SUCCESS**: The operation is successful.

**VK\_ERROR\_OUT\_OF\_HOST\_MEMORY**: The input parameter **pInfo** is abnormal or the obtained **pBuffer** is abnormal.

 |

#### \[h2\]vkGetSwapchainGrallocUsageOHOS()

VKAPI\_ATTR VkResult VKAPI\_CALL vkGetSwapchainGrallocUsageOHOS(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64\_t\* grallocUsage)

**Description**

Returns the appropriate gralloc usage flag based on the given Vulkan device, image format, and image usage flag.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| VkDevice device | VkDevice object. |
| VkFormat format | Image format. |
| VkImageUsageFlags imageUsage | Image use flag. |
| uint64\_t\* grallocUsage | Pointer to the gralloc usage flag. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | 
One of the following error codes of the VkResult type:

**VK\_SUCCESS**: The operation is successful.

**VK\_ERROR\_INITIALIZATION\_FAILED**: An input parameter is abnormal.

 |

#### \[h2\]VKAPI\_PTR \*PFN\_vkGetSwapchainGrallocUsageOHOS()

typedef VkResult (VKAPI\_PTR \*PFN\_vkGetSwapchainGrallocUsageOHOS)(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64\_t\* grallocUsage)

**Description**

Returns the appropriate gralloc usage flag based on the given Vulkan device, image format, and image usage flag. As an application developer, you do not need to use this function.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Deprecated from**: 23

**Parameters**

| Name | Description |
| :-- | :-- |
| VkDevice device | VkDevice object. |
| VkFormat format | Image format. |
| VkImageUsageFlags imageUsage | Image use flag. |
| uint64\_t\* grallocUsage | Pointer to the gralloc usage flag. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | 
One of the following error codes of the VkResult type:

**VK\_SUCCESS**: The operation is successful.

**VK\_ERROR\_INITIALIZATION\_FAILED**: An input parameter is abnormal.

 |

#### \[h2\]vkAcquireImageOHOS()

VKAPI\_ATTR VkResult VKAPI\_CALL vkAcquireImageOHOS(VkDevice device, VkImage image, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)

**Description**

Obtains the ownership of the swap chain image and imports the fence of the external signal to the VkSemaphore and VkFence objects.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| VkDevice device | VkDevice object. |
| VkImage image | Vulkan image to obtain. |
| int32\_t nativeFenceFd | File descriptor of the native fence. |
| VkSemaphore semaphore | Vulkan semaphore indicating that the image is available. |
| VkFence fence | Vulkan fence used for synchronization when the image acquisition is complete. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | 
One of the following error codes of the VkResult type:

**VK\_SUCCESS**: The operation is successful.

**VK\_ERROR\_OUT\_OF\_HOST\_MEMORY**: The host memory is insufficient.

 |

#### \[h2\]VKAPI\_PTR \*PFN\_vkAcquireImageOHOS()

typedef VkResult (VKAPI\_PTR \*PFN\_vkAcquireImageOHOS)(VkDevice device, VkImage image, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)

**Description**

Obtains the ownership of the swap chain image and imports the fence of the external signal to the VkSemaphore and VkFence objects. As an application developer, you do not need to use this function.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Deprecated from**: 23

**Parameters**

| Name | Description |
| :-- | :-- |
| VkDevice device | VkDevice object. |
| VkImage image | Vulkan image to obtain. |
| int32\_t nativeFenceFd | File descriptor of the native fence. |
| VkSemaphore semaphore | Vulkan semaphore indicating that the image is available. |
| VkFence fence | Vulkan fence used for synchronization when the image acquisition is complete. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | 
One of the following error codes of the VkResult type:

**VK\_SUCCESS**: The operation is successful.

**VK\_ERROR\_OUT\_OF\_HOST\_MEMORY**: The host memory is insufficient.

 |

#### \[h2\]vkQueueSignalReleaseImageOHOS()

VKAPI\_ATTR VkResult VKAPI\_CALL vkQueueSignalReleaseImageOHOS(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore\* pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)

**Description**

Sends a signal to the system hardware buffer to release an image once it is no longer needed so that other components can access it.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| VkQueue queue | Handle to the Vulkan queue. |
| uint32\_t waitSemaphoreCount | Number of semaphores to wait on. |
| const VkSemaphore\* pWaitSemaphores | Pointer to the array of semaphores to wait on. |
| VkImage image | Handle to the Vulkan image to be released. |
| int32\_t\* pNativeFenceFd | Pointer to the file descriptor of the fence. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | 
One of the following error codes of the VkResult type:

**VK\_SUCCESS**: The operation is successful.

**VK\_ERROR\_DEVICE\_LOST**: The Vulkan device link is lost.

**VK\_ERROR\_OUT\_OF\_HOST\_MEMORY**: The host memory is insufficient.

 |

#### \[h2\]VKAPI\_PTR \*PFN\_vkQueueSignalReleaseImageOHOS()

typedef VkResult (VKAPI\_PTR \*PFN\_vkQueueSignalReleaseImageOHOS)(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore\* pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)

**Description**

Sends a signal to the system hardware buffer to release an image once it is no longer needed so that other components can access it. As an application developer, you do not need to use this function.

**System capability**: SystemCapability.Graphic.Vulkan

**Since**: 10

**Deprecated from**: 23

**Parameters**

| Name | Description |
| :-- | :-- |
| VkQueue queue | Handle to the Vulkan queue. |
| uint32\_t waitSemaphoreCount | Number of semaphores to wait on. |
| const VkSemaphore\* pWaitSemaphores | Pointer to the array of semaphores to wait on. |
| images | Handle to the Vulkan image to be released. |
| int32\_t\* pNativeFenceFd | Pointer to the file descriptor of the fence. |

**Returns**

| Type | Description |
| :-- | :-- |
| VkResult | 
One of the following error codes of the VkResult type:

**VK\_SUCCESS**: The operation is successful.

**VK\_ERROR\_DEVICE\_LOST**: The Vulkan device link is lost.

**VK\_ERROR\_OUT\_OF\_HOST\_MEMORY**: The host memory is insufficient.

 |

## VKAPI\_PTR \*PFN\_vkSetNativeFenceFdOpenHarmony()

typedef VkResult (VKAPI\_PTR \*PFN\_vkSetNativeFenceFdOpenHarmony)(VkDevice device, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)

**Description**

This API has been deprecated.

**Since**: 10

**Deprecated from**: 10

**Substitute**: [PFN\_vkAcquireImageOHOS](#vkapi_ptr-pfn_vkacquireimageohos)

## VKAPI\_PTR \*PFN\_vkGetNativeFenceFdOpenHarmony()

typedef VkResult (VKAPI\_PTR \*PFN\_vkGetNativeFenceFdOpenHarmony)(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore\* pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)

**Description**

This API has been deprecated.

**Since**: 10

**Deprecated from**: 10

**Substitute**: [PFN\_vkQueueSignalReleaseImageOHOS](#vkapi_ptr-pfn_vkqueuesignalreleaseimageohos)

## vkSetNativeFenceFdOpenHarmony()

VKAPI\_ATTR VkResult VKAPI\_CALL vkSetNativeFenceFdOpenHarmony(VkDevice device, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)

**Description**

This API has been deprecated.

**Since**: 10

**Deprecated from**: 10

**Substitute**: [vkAcquireImageOHOS](#vkacquireimageohos)

## vkGetNativeFenceFdOpenHarmony()

VKAPI\_ATTR VkResult VKAPI\_CALL vkGetNativeFenceFdOpenHarmony(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore\* pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)

**Description**

This API has been deprecated.

**Since**: 10

**Deprecated from**: 10

**Substitute**: [vkQueueSignalReleaseImageOHOS](#vkqueuesignalreleaseimageohos)
