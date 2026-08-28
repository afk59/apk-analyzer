# NativeBuffer Development (C/C++)

#### Overview

The NativeBuffer module provides the **shared memory** feature, supporting memory application, use, query, and release.

Common development scenarios of NativeBuffer: Apply for **OH\_NativeBuffer** instances through Native APIs, obtain memory properties, and map the ION memory to the process space.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_NativeBuffer\_Alloc (const OH\_NativeBuffer\_Config \*config) | Creates an **OH\_NativeBuffer** instance based on an **OH\_NativeBuffer\_Config** struct. A new **OH\_NativeBuffer** instance is created each time this function is called. This function must be used in pair with **OH\_NativeBuffer\_Unreference**. Otherwise, memory leak occurs. |
| OH\_NativeBuffer\_Reference (OH\_NativeBuffer \*buffer) | Increases the reference count of an **OH\_NativeBuffer** instance by 1. |
| OH\_NativeBuffer\_Unreference (OH\_NativeBuffer \*buffer) | Decreases the reference count of an **OH\_NativeBuffer** instance by 1 and, when the reference count reaches 0, destroys the instance. |
| OH\_NativeBuffer\_GetConfig (OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_Config \*config) | Obtains the properties of an **OH\_NativeBuffer** instance. |
| OH\_NativeBuffer\_Map (OH\_NativeBuffer \*buffer, void \*\*virAddr) | Maps the ION memory allocated to an **OH\_NativeBuffer** instance to the process address space. |
| OH\_NativeBuffer\_Unmap (OH\_NativeBuffer \*buffer) | Unmaps the ION memory allocated to an **OH\_NativeBuffer** instance from the process address space. |
| OH\_NativeBuffer\_GetSeqNum (OH\_NativeBuffer \*buffer) | Obtains the sequence number of an **OH\_NativeBuffer** instance. |

For details about the APIs, see [native\_buffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-nativebuffer).

#### How to Develop

The following describes how to use the aforementioned APIs to create an **OH\_NativeBuffer** instance, obtain memory properties, and map the ION memory to the process address space.

**Adding Dynamic Link Libraries**

Add the following library to **CMakeLists.txt**:

libnative\_buffer.so

**Including Header Files**

#include <native\_buffer/native\_buffer.h>

1.  Create an **OH\_NativeBuffer** instance.
    
    OH\_NativeBuffer\_Config config {
        .width = 0x100,
        .height = 0x100,
        .format = NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888,
        .usage = NATIVEBUFFER\_USAGE\_CPU\_READ | NATIVEBUFFER\_USAGE\_CPU\_WRITE | NATIVEBUFFER\_USAGE\_MEM\_DMA,
    };
    
    OH\_NativeBuffer \*nativeBuffer = OH\_NativeBuffer\_Alloc(&config);
    if (nativeBuffer == nullptr) {
        LOGE("OH\_NativeBuffer\_Alloc fail, nativeBuffer is null");
    }
    
2.  Map the ION memory allocated to an **OH\_NativeBuffer** instance to the process address space.
    
    Call **OH\_NativeBuffer\_Map** if the application needs to access the memory space of the buffer.
    
    void\* virAddr = nullptr;
    int32\_t ret = OH\_NativeBuffer\_Map(nativeBuffer, &virAddr);
    if (ret != 0) {
        LOGE("OH\_NativeBuffer\_Map Failed");
    }
    // ···
    ret = OH\_NativeBuffer\_Unmap(nativeBuffer);
    if (ret != 0) {
        LOGE("OH\_NativeBuffer\_Unmap Failed");
    }
    
3.  Obtain the memory properties.
    
    OH\_NativeBuffer\_Config config2 = {};
    OH\_NativeBuffer\_GetConfig(nativeBuffer, &config2);
    uint32\_t hwBufferID = OH\_NativeBuffer\_GetSeqNum(nativeBuffer);
    
4.  Destroy the **OH\_NativeBuffer** instance.
    
    OH\_NativeBuffer\_Unreference(nativeBuffer);
    nativeBuffer = nullptr;
