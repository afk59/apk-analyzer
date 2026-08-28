# NativeVSync Development (C/C++)

#### Overview

The NativeVSync module is used to obtain the system VSync signal, create and destroy an **OH\_NativeVSync** instance, and set the VSync callback function. When the VSync signal is triggered, the callback function is called.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_NativeVSync\_Create (const char \*name, unsigned int length) | Creates an **OH\_NativeVSync** instance. Each call creates an instance and a VSync thread to receive and process the callback. This function must be used in pair with **OH\_NativeVSync\_Destroy**. Otherwise, memory leak occurs. |
| OH\_NativeVSync\_Destroy (OH\_NativeVSync \*nativeVsync) | Destroys an **OH\_NativeVSync** instance. |
| OH\_NativeVSync\_FrameCallback (long long timestamp, void \*data) | Sets a callback function. **timestamp** indicates the timestamp, and **data** indicates a pointer to the input parameters of the callback function. The callback is processed in the thread created during VSync initialization. |
| OH\_NativeVSync\_RequestFrame (OH\_NativeVSync \*nativeVsync, OH\_NativeVSync\_FrameCallback callback, void \*data) | Requests the next VSync signal. When the signal arrives, a callback function is invoked. |

For details about the APIs, see [native\_vsync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativevsync).

#### How to Develop

The following steps describe how to use the native APIs provided by NativeVSync to create and destroy an **OH\_NativeVSync** instance and set the VSync callback function.

**Adding Dynamic Link Libraries**

Add the following library file to the **CMakeLists.txt** file.

libnative\_vsync.so

**Including Header Files**

#include <native\_vsync/native\_vsync.h>

1.  Define a VSync callback function.
    
    void RenderEngine::OnVsync(long long timestamp, void \*data)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_DEBUG, LOG\_PRINT\_DOMAIN, "RenderEngine", "OnVsync %{public}lld.", timestamp);
        auto renderEngine = reinterpret\_cast<RenderEngine \*>(data);
        if (renderEngine == nullptr) {
            return;
        }
    
        renderEngine->vSyncCnt\_++;
        renderEngine->wakeUpCond\_.notify\_one();
    }
    
2.  Create an **OH\_NativeVSync** instance.
    
    const char\* demoName = "NativeImageSample";
    nativeVsync\_ = OH\_NativeVSync\_Create(demoName, strlen(demoName));
    
3.  Set the VSync callback function through the **OH\_NativeVSync** instance.
    
    wakeUpCond\_.wait(lock, \[this\]() { return wakeUp\_ || vSyncCnt\_ > 0; });
    wakeUp\_ = false;
    if (vSyncCnt\_ > 0) {
        vSyncCnt\_--;
        (void)OH\_NativeVSync\_RequestFrame(nativeVsync\_, &RenderEngine::OnVsync, this);
        OH\_NativeVSync\_GetPeriod(nativeVsync\_, &period);
    }
    
4.  Destroy the **OH\_NativeVSync** instance.
    
    OH\_NativeVSync\_Destroy(nativeVsync\_);
    nativeVsync\_ = nullptr;
