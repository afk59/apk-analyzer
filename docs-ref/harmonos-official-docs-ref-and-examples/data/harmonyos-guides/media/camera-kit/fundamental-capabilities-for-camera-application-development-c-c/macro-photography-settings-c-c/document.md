# Macro Photography Settings (C/C++)

Starting from API version 19, you can configure macro photography. This feature allows the camera to focus closely and capture detailed images of small objects through optimized optical design and algorithms.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera) for the API reference.

1.  Import the NDK.
    
    #include <cstdint>
    #include <native\_buffer/buffer\_common.h>
    #include <unistd.h>
    #include <string>
    #include <thread>
    #include <cstdio>
    #include <fcntl.h>
    #include <map>
    #include <string>
    #include <vector>
    #include <native\_buffer/native\_buffer.h>
    #include "iostream"
    #include "mutex"
    
    #include "hilog/log.h"
    #include "ohcamera/camera.h"
    #include "ohcamera/camera\_input.h"
    #include "ohcamera/capture\_session.h"
    #include "ohcamera/photo\_output.h"
    #include "ohcamera/preview\_output.h"
    #include "ohcamera/video\_output.h"
    #include "napi/native\_api.h"
    #include "ohcamera/camera\_manager.h"
    #include <window\_manager/oh\_display\_info.h>
    #include <window\_manager/oh\_display\_manager.h>
    
    namespace OHOS\_CAMERA\_SAMPLE {
    class NDKCamera {
      public:
        struct CameraBuildingConfig {
            char \*str;
            uint32\_t focusMode;
            uint32\_t cameraDeviceIndex;
            bool isVideo;
            bool isHdr;
            char \*videoId;
        };
        ~NDKCamera();
        explicit NDKCamera(CameraBuildingConfig config);
        // ...
    };
    } // namespace OHOS\_CAMERA\_SAMPLE
    
2.  Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(entry PUBLIC
        libace\_napi.z.so
        libohcamera.so
        libhilog\_ndk.z.so
    )
    
3.  Call [OH\_CaptureSession\_IsMacroSupported()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_ismacrosupported) to check whether the current device supports macro photography.
    
    bool NDKCamera::IsMacroSupported(Camera\_CaptureSession\* captureSession)
    {
        // Check whether the device supports macro photography.
        bool isMacroSupported = false;
        if (captureSession == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "IsMacroSupported: session is nullptr.");
            return isMacroSupported;
        }
        Camera\_ErrorCode ret = OH\_CaptureSession\_IsMacroSupported(captureSession, &isMacroSupported);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_IsMacroSupported failed.");
        }
        if (isMacroSupported) {
            OH\_LOG\_INFO(LOG\_APP, "support macro capability.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "No support macro capability.");
        }
        return isMacroSupported;
    }
    
4.  Call [OH\_CaptureSession\_EnableMacro()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_enablemacro) to enable or disable macro photography.
    
    void NDKCamera::EnableMacro(bool isMacro)
    {
        OH\_LOG\_INFO(LOG\_APP, "EnableMacro: isMacro is %{public}d", isMacro);
        if (IsMacroSupported(captureSession\_)) {
            Camera\_ErrorCode ret = OH\_CaptureSession\_EnableMacro(captureSession\_, isMacro);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_EnableMacro failed.");
            }
        }
    }
    

#### Status Listening

Starting from API version 20, you can listen for macro photography status changes.

Call [OH\_CaptureSession\_RegisterMacroStatusChangeCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_registermacrostatuschangecallback) to register a callback for listening.

void MacroStatusCallback(Camera\_CaptureSession \*captureSession, bool isMacroDetected)
{
    OH\_LOG\_INFO(LOG\_APP, "MacroStatusCallback isMacro: %{public}d", isMacroDetected);
}

// Register a callback.
Camera\_ErrorCode NDKCamera::RegisterMacroStatusCallback()
{
    Camera\_ErrorCode ret = OH\_CaptureSession\_RegisterMacroStatusChangeCallback(captureSession\_, MacroStatusCallback);
    if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_RegisterMacroStatusChangeCallback failed.");
    }
    return ret;
}

// Unregister the callback.
Camera\_ErrorCode NDKCamera::UnregisterMacroStatusCallback()
{
    Camera\_ErrorCode ret = OH\_CaptureSession\_UnregisterMacroStatusChangeCallback(captureSession\_, MacroStatusCallback);
    if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_UnregisterMacroStatusChangeCallback failed.");
    }
    return ret;
}
