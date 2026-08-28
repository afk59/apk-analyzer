# Native Window Development (C/C++)

#### Overview

The native window module is a local platform-based window that represents the producer of a graphics queue. It provides APIs for you to request and flush a buffer and configure buffer attributes.

The following scenarios are common for native window development:

-   Apply for a graphics Buffer through the Native API provided by NativeWindow, write the generated graphics content to the graphics Buffer, and submit the Buffer to the graphics queue.
-   Request and flush a buffer when adapting to the **eglswapbuffer** interface at the EGL.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_NativeWindow\_NativeWindowRequestBuffer (OHNativeWindow \*window, OHNativeWindowBuffer \*\*buffer, int \*fenceFd) | Requests an **OHNativeWindowBuffer** through an **OHNativeWindow** instance for content production. |
| OH\_NativeWindow\_NativeWindowFlushBuffer (OHNativeWindow \*window, OHNativeWindowBuffer \*buffer, int fenceFd, Region region) | Flushes the **OHNativeWindowBuffer** filled with the produced content to the buffer queue through an **OHNativeWindow** instance for content consumption. |
| OH\_NativeWindow\_NativeWindowHandleOpt (OHNativeWindow \*window, int code,...) | Sets or obtains the attributes of an **OHNativeWindow** instance, including the width, height, and content format. |

For details, see [native\_window](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativewindow).

#### How to Develop

The following procedure describes how to use the native APIs provided by NativeWindow to apply for a graphics buffer, write graphics content, and submit the buffer to the graphics queue.

**Adding Dynamic Link Libraries**

Add the following libraries to **CMakeLists.txt**:

libace\_ndk.z.so
libnative\_window.so

**Including Header Files**

#include <sys/poll.h>
#include <sys/mman.h>
#include <unistd.h>
#include <ace/xcomponent/native\_interface\_xcomponent.h>
#include <native\_window/external\_window.h>

1.  Obtain an **OHNativeWindow** instance.
    
    You can obtain the OHNativeWindow through the [OH\_NativeXComponent\_Callback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback) API. The sample code is as follows: For details about how to use the XComponent module, see [XComponent Development Guidelines](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/adding-a-component/custom-rendering-xcomponent/document.md).
    
    1.  Add an **XComponent** to the .ets file.
        
        XComponent({ id: 'xcomponentId', type: 'texture', libraryname: 'nativerender' })
            .margin({ bottom: 26 })
            .onLoad((nativeWindowContext) => {
            this.nativeWindowContext = nativeWindowContext as NativeWindowContext;
            })
        
    2.  Obtain **NativeXComponent** at the native C++ layer.
        
        napi\_value exportInstance = nullptr;
        OH\_NativeXComponent \*nativeXComponent = nullptr;
        int32\_t ret;
        char idStr\[OH\_XCOMPONENT\_ID\_LEN\_MAX + 1\] = {};
        uint64\_t idSize = OH\_XCOMPONENT\_ID\_LEN\_MAX + 1;
        
        status = napi\_get\_named\_property(env, exports, OH\_NATIVE\_XCOMPONENT\_OBJ, &exportInstance);
        if (status != napi\_ok) {
            return false;
        }
        
        status = napi\_unwrap(env, exportInstance, reinterpret\_cast<void\*\*>(&nativeXComponent));
        if (status != napi\_ok) {
            return false;
        }
        
        ret = OH\_NativeXComponent\_GetXComponentId(nativeXComponent, idStr, &idSize);
        if (ret != OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) {
            return false;
        }
        
    3.  Define **OH\_NativeXComponent\_Callback**.
        
        void OnSurfaceCreatedCB(OH\_NativeXComponent\* component, void\* window)
        {
            // ···
            OHNativeWindow\* nativeWindow = static\_cast<OHNativeWindow\*>(window);
            // ···
        }
        
        void OnSurfaceChangedCB(OH\_NativeXComponent\* component, void\* window)
        {
            // ···
            OHNativeWindow\* nativeWindow = static\_cast<OHNativeWindow\*>(window);
            // ···
        }
        
        void OnSurfaceDestroyedCB(OH\_NativeXComponent\* component, void\* window)
        {
            // ···
            OHNativeWindow\* nativeWindow = static\_cast<OHNativeWindow\*>(window);
            // ···
        }
        
        void DispatchTouchEventCB(OH\_NativeXComponent\* component, void\* window)
        {
            // ···
            OHNativeWindow\* nativeWindow = static\_cast<OHNativeWindow\*>(window);
        }
        // ···
        callback\_.OnSurfaceCreated = OnSurfaceCreatedCB;
        callback\_.OnSurfaceChanged = OnSurfaceChangedCB;
        callback\_.OnSurfaceDestroyed = OnSurfaceDestroyedCB;
        callback\_.DispatchTouchEvent = DispatchTouchEventCB;
        
    4.  Register **OH\_NativeXComponent\_Callback** with **NativeXComponent**.
        
        OH\_NativeXComponent\_RegisterCallback(nativeXComponent, &callback\_);
        
2.  Set the attributes of an **OHNativeWindowBuffer** Use OH\_NativeWindow\_NativeWindowHandleOpt to set the attributes of OHNativeWindowBuffer. (By default, the NATIVEBUFFER\_USAGE\_CPU\_READ usage parameter is carried. If the CPU is not used to read and write data, you are advised to remove the NATIVEBUFFER\_USAGE\_CPU\_READ usage parameter. For details, see [Disabling CPU Access to Window Buffer Data](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-14).)
    
    int code = SET\_BUFFER\_GEOMETRY;
    int32\_t bufferHeight = static\_cast<int32\_t>(height\_ / 4);
    int32\_t bufferWidth = static\_cast<int32\_t>(width\_ / 2);
    OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow\_, code, bufferWidth, bufferHeight);
    
3.  Request an **OHNativeWindowBuffer** from the graphics queue.
    
    int fenceFd = -1;
    OHNativeWindowBuffer \*nativeWindowBuffer = nullptr;
    ret = OH\_NativeWindow\_NativeWindowRequestBuffer(nativeWindow, &nativeWindowBuffer, &fenceFd);
    if (ret != 0 || nativeWindowBuffer == nullptr) {
        return;
    }
    BufferHandle \*bufferHandle = OH\_NativeWindow\_GetBufferHandleFromNative(nativeWindowBuffer);
    
4.  Map memory.
    
    void \*mappedAddr =
        mmap(bufferHandle->virAddr, bufferHandle->size, PROT\_READ | PROT\_WRITE, MAP\_SHARED, bufferHandle->fd, 0);
    
5.  Write the produced content to the **OHNativeWindowBuffer**. Before this operation, wait until **releaseFenceFd** is available. (Note that **poll** needs to be called only when **releaseFenceFd** is not **\-1**.) If no data waiting for **releaseFenceFd** is available (POLLIN), problems such as artifacts, cracks, and High Efficiency Bandwidth Compression (HEBC) faults may occur. **releaseFenceFd** is a file handle created by the consumer process to indicate that the consumer has consumed the buffer, the buffer is readable, and the producer can start to fill in the buffer.
    
    int retCode = -1;
    uint32\_t timeout = 3000;
    if (fenceFd != -1) {
        struct pollfd pollfds = {0};
        pollfds.fd = fenceFd;
        pollfds.events = POLLIN;
        do {
            retCode = poll(&pollfds, 1, timeout);
        } while (retCode == -1 && (errno == EINTR || errno == EAGAIN));
        close(fenceFd);
    }
    uint32\_t \*pixel = static\_cast<uint32\_t \*>(mappedAddr);
    for (uint64\_t x = 0; x < bufferHandle->width; x++) {
        for (uint64\_t y = 0; y < bufferHandle->height; y++) {
            \*pixel++ = value;
        }
    }
    
6.  Flush the **OHNativeWindowBuffer** to the graphics queue. Note that **acquireFenceFd** of **OH\_NativeWindow\_NativeWindowFlushBuffer** cannot be the same as **releaseFenceFd** obtained by **OH\_NativeWindow\_NativeWindowRequestBuffer**. **acquireFenceFd** is the file handle passed in by the producer, and the default value **\-1** can be passed. Based on **acquireFenceFd**, the consumer, after obtaining the buffer, determines when to render and display the buffered content.
    
    struct Region \*region = new Region();
    ret = OH\_NativeWindow\_NativeWindowFlushBuffer(nativeWindow, nativeWindowBuffer, fenceFd, \*region);
    if (ret != NATIVE\_ERROR\_OK) {
        LOGE("flush failed");
        (void)OH\_NativeWindow\_NativeWindowAbortBuffer(nativeWindow, nativeWindowBuffer);
        return;
    }
    
7.  Unmaps memory using munmap.
    
    if (munmap(mappedAddr, bufferHandle->size) < 0) {
        OH\_NativeWindow\_DestroyNativeWindow(nativeWindow);
        LOGE("munmap failed");
        return;
    }
