# Vulkan Surface Development

#### When to Use

In HarmonyOS, the VK\_OHOS\_surface extension enables the creation of a VkSurfaceKHR, which connects to the OHNativeWindow module to implement the rotation of OHNativeBuffers for display purposes.

A VkSurfaceKHR instance is obtained through an OHNativeWindow, which is obtained from the **XComponent**. Therefore, the OHNativeWindow module must be used together with the **XComponent** and NativeWindow modules. For specific usage of the **XComponent**, see [Custom Rendering (XComponent)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-xcomponent-guidelines).

#### Available APIs

| API | Description |
| :-- | :-- |
| vkCreateSurfaceOHOS (VkInstance instance, const VkSurfaceCreateInfoOHOS\* pCreateInfo, const VkAllocationCallbacks\* pAllocator, VkSurfaceKHR\* pSurface) | Creates a VkSurfaceKHR instance. |

For details about the APIs, see [Vulkan](../../vulkan-capabilities/document.md).

#### How to Develop

The following steps illustrate how to create a VkSurfaceKHR instance.

**HarmonyOS Platform Macro**

To use the extension, you must define the macro **VK\_USE\_PLATFORM\_OHOS** in the **CMakeLists.txt** file.

ADD\_DEFINITIONS(-DVK\_USE\_PLATFORM\_OHOS=1)

**Adding Dynamic Link Libraries**

Add the Vulkan library and associated module libraries in the **CMakeLists.txt** file.

libvulkan.so
libace\_ndk.z.so
libnative\_window.so
libnative\_image.so
libnative\_buffer.so

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/B-UoHJ-ZSWutL51WIaHiQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062528Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF2FF2D55E12A1E7D95178E7EAF22F84CA11B16F65CB9EB49655B89D2CD65812)

When the **dlopen** function is used to link the **libvulkan.so** dynamic library in a program, you do not need to add dependencies in CMake. Otherwise, symbol conflicts occur.

**Including Header Files**

#include <ace/xcomponent/native\_interface\_xcomponent.h>
#include <native\_window/external\_window.h>
#include <vulkan/vulkan.h>

1.  Create a Vulkan instance.
    
    VkInstance instance = VK\_NULL\_HANDLE;
    
    VkApplicationInfo appInfo = {};
    appInfo.sType = VK\_STRUCTURE\_TYPE\_APPLICATION\_INFO;
    appInfo.pApplicationName = "vulkanExample";
    appInfo.pEngineName = "vulkanExample";
    appInfo.apiVersion = VK\_API\_VERSION\_1\_3;
    
    VkInstanceCreateInfo instanceCreateInfo = {};
    instanceCreateInfo.sType = VK\_STRUCTURE\_TYPE\_INSTANCE\_CREATE\_INFO;
    instanceCreateInfo.pNext = NULL;
    instanceCreateInfo.pApplicationInfo = &appInfo;
    
    std::vector<const char \*> instanceExtensions = {
        VK\_KHR\_SURFACE\_EXTENSION\_NAME,
        VK\_OHOS\_SURFACE\_EXTENSION\_NAME // Surface extension.
    };
    instanceCreateInfo.enabledExtensionCount = static\_cast<uint32\_t>(instanceExtensions.size());
    instanceCreateInfo.ppEnabledExtensionNames = instanceExtensions.data();
    
    vkCreateInstance(&instanceCreateInfo, nullptr, &instance);
    
2.  Obtain an OHNativeWindow instance.
    
    The OHNativeWindow instance is obtained from the **XComponent**. For details about how to use the **XComponent**, see [Custom Rendering (XComponent)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-xcomponent-guidelines).
    
    1.  Add an **XComponent** to **ets/pages/Index.ets**.
        
        XComponent({
            id: 'xcomponentId',
            type: 'surface',
            libraryname: 'entry'
        })
        .margin({ bottom: 20 })
        .width(360)
        .height(360)
        
    2.  Obtain an OHNativeWindow instance from the **XComponent**.
        
        // Callback function of the XComponent triggered when a surface is created.
        void OnSurfaceCreatedCB(OH\_NativeXComponent \*component, void \*window) {
            // You can obtain an OHNativeWindow instance from the callback function.
            OHNativeWindow \*nativeWindow = static\_cast<OHNativeWindow \*>(window);
        }
        
        static napi\_value Init(napi\_env env, napi\_value exports) {
            napi\_property\_descriptor desc\[\] = {{"add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr}};
            napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        
            napi\_value exportInstance = nullptr;
            OH\_NativeXComponent \*nativeXComponent = nullptr;
            // Obtain a native XComponent.
            napi\_get\_named\_property(env, exports, OH\_NATIVE\_XCOMPONENT\_OBJ, &exportInstance);
            napi\_unwrap(env, exportInstance, reinterpret\_cast<void \*\*>(&nativeXComponent));
            // Obtain the XComponent ID.
            char idStr\[OH\_XCOMPONENT\_ID\_LEN\_MAX + 1\] = {};
            uint64\_t idSize = OH\_XCOMPONENT\_ID\_LEN\_MAX + 1;
            OH\_NativeXComponent\_GetXComponentId(nativeXComponent, idStr, &idSize);
        
            // Declare an XComponent callback.
            OH\_NativeXComponent\_Callback callback;
            // Register the OnSurfaceCreated callback function.
            callback.OnSurfaceCreated = OnSurfaceCreatedCB;
            // Register the callback function for the native XComponent.
            OH\_NativeXComponent\_RegisterCallback(nativeXComponent, &callback);
        
            return exports;
        }
        
3.  Create a VkSurfaceKHR instance.
    
    VkSurfaceKHR surface = VK\_NULL\_HANDLE;
    VkSurfaceCreateInfoOHOS surfaceCreateInfo = {};
    surfaceCreateInfo.sType = VK\_STRUCTURE\_TYPE\_SURFACE\_CREATE\_INFO\_OHOS;
    surfaceCreateInfo.window = nativeWindow; // nativeWindow is obtained from the OnSurfaceCreatedCB callback function in the previous step.
    int err = vkCreateSurfaceOHOS(instance, &surfaceCreateInfo, NULL, &surface);
    if (err != VK\_SUCCESS) {
        // Creating the surface failed.
    }
