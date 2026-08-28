# Preview (C/C++)

Preview is the image you see after you start the camera application but before you take photos or record videos.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera) for the API reference.

1.  Import the NDK, which provides camera-related properties and methods.
    
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
    
2.  Link the dynamic library in the CMake script.
    
    target\_link\_libraries(entry PUBLIC
        libace\_napi.z.so
        libohcamera.so
        libhilog\_ndk.z.so
    )
    
3.  Obtain the surface ID.
    
    The **XComponent**, the capabilities of which are provided by the UI, offers the surface ID for preview streams. For details, see [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).
    
4.  Call [OH\_CameraManager\_GetSupportedCameraOutputCapability()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameraoutputcapability) to obtain the preview capability supported by the current device based on the surface ID. Then call [OH\_CameraManager\_CreatePreviewOutput()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createpreviewoutput) to create a PreviewOutput instance, with the parameters set to the **cameraManager** pointer, the first item in the **previewProfiles** array, the surface ID obtained in step 3, and the returned **previewOutput** pointer, respectively.
    
    Camera\_ErrorCode NDKCamera::CreatePreviewOutput(void)
    {
        if (previewProfile\_ == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "Get previewProfiles failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CameraManager\_CreatePreviewOutput(cameraManager\_, previewProfile\_, previewSurfaceId\_, &previewOutput\_);
        OH\_LOG\_ERROR(LOG\_APP, "create preview width: %{public}d, height: %{public}d, format: %{public}d",
            previewProfile\_->size.width, previewProfile\_->size.height, previewProfile\_->format);
        if (previewSurfaceId\_ == nullptr || previewOutput\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "CreatePreviewOutput failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        return ret\_;
        PreviewOutputRegisterCallback();
    }
    
5.  Configure the session. Call **commitConfig()** to commit the session configuration, and then call [OH\_CaptureSession\_Start()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_start) to start outputting the preview stream. If the call fails, an error code is returned. For details, see [Camera\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_errorcode).
    
    Camera\_ErrorCode NDKCamera::SessionStart(void)
    {
        Camera\_ErrorCode ret = OH\_CaptureSession\_Start(captureSession\_);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_Start success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Start failed. %d ", ret);
        }
        return ret;
    }
    
6.  Call [OH\_CaptureSession\_Stop()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_stop) to stop outputting the preview stream. If the call fails, an error code is returned. For details, see[Camera\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_errorcode).
    
    Camera\_ErrorCode NDKCamera::SessionStop(void)
    {
        Camera\_ErrorCode ret = OH\_CaptureSession\_Stop(captureSession\_);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_Stop success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Stop failed. %d ", ret);
        }
        return ret;
    }
    

#### Status Listening

During camera application development, you can listen for the preview output stream status, including preview stream start, preview stream end, and preview stream output errors.

-   Register the **'frameStart'** event to listen for preview start events. This event can be registered when a PreviewOutput object is created and is triggered when the bottom layer starts exposure for the first time. The preview stream starts as long as a result is returned.
    
    void PreviewOutputOnFrameStart(Camera\_PreviewOutput \*previewOutput)
    {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutputOnFrameStart");
    }
    
-   Register the **'frameEnd'** event to listen for preview end events. This event can be registered when a PreviewOutput object is created and is triggered when the last frame of preview ends. The preview stream ends as long as a result is returned.
    
    void PreviewOutputOnFrameEnd(Camera\_PreviewOutput \*previewOutput, int32\_t frameCount)
    {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutput frameCount = %{public}d", frameCount);
    }
    
-   Register the **'error'** event to listen for preview output errors. The callback function returns an error code when an API is incorrectly used. For details about the error code types, see [Camera\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_errorcode).
    
    void PreviewOutputOnError(Camera\_PreviewOutput \*previewOutput, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutput errorCode = %{public}d", errorCode);
    }
    
    PreviewOutput\_Callbacks \*NDKCamera::GetPreviewOutputListener(void)
    {
        static PreviewOutput\_Callbacks previewOutputListener = {
            .onFrameStart = PreviewOutputOnFrameStart,
            .onFrameEnd = PreviewOutputOnFrameEnd,
            .onError = PreviewOutputOnError
        };
        return &previewOutputListener;
    }
    
    Camera\_ErrorCode NDKCamera::PreviewOutputRegisterCallback(void)
    {
        ret\_ = OH\_PreviewOutput\_RegisterCallback(previewOutput\_, GetPreviewOutputListener());
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PreviewOutput\_RegisterCallback failed.");
        }
        return ret\_;
    }
