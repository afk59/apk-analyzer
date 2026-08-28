# Using Camera Preconfiguration (C/C++)

The camera preconfiguration (preconfig) feature streamlines the development of camera applications by offering preset configurations for typical use cases and resolutions, enhancing the efficiency of the development process.

Following the general development process, it is complex to develop a camera application after obtaining a camera device. Specifically, you need to query the output configurations supported by the current camera in the specified mode, parse and filter the data in the obtained [Camera\_OutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-outputcapability) to find the required [Camera\_Profile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-profile) and [Camera\_VideoProfile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-videoprofile), and use the corresponding profiles to create [Camera\_PreviewOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-previewoutput), [Camera\_PhotoOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-photooutput), and [Camera\_VideoOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-videooutput).

To streamline this process, the system provides the [OH\_CameraManager\_CreatePreviewOutputUsedInPreconfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createpreviewoutputusedinpreconfig), [OH\_CameraManager\_CreatePhotoOutputUsedInPreconfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createphotooutputusedinpreconfig), and [OH\_CameraManager\_CreateVideoOutputUsedInPreconfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createvideooutputusedinpreconfig) APIs for you to quickly set camera parameters in the photo capture and video recording scenarios (where [Camera\_SceneMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_scenemode) is **NORMAL\_PHOTO** or **NORMAL\_VIDEO**). It is recommended that you use the preconfig feature to speed up the application development cycle if you only need to customize the camera UI without the need for advanced camera application development.

#### Specifications

The system provides four preconfiguration types (specified by [Camera\_PreconfigType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_preconfigtype)): **PRECONFIG\_720P**, **PRECONFIG\_1080P**, **PRECONFIG\_4K**, and **PRECONFIG\_HIGH\_QUALITY**. It also provides three aspect ratio specifications (specified by [Camera\_PreconfigRatio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_preconfigratio)): 1:1 (**PRECONFIG\_RATIO\_1\_1**), 4:3 (**PRECONFIG\_RATIO\_4\_3**), and 16:9 (**PRECONFIG\_RATIO\_16\_9**).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Im5T7okaSFylT1mE_q4BAQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E11FA8A08E04FA778EEA6E730AA28B71F639E865C414EA541FA2674881C34B7F)

The capabilities supported vary according to the device. Before using preconfig, call [OH\_CaptureSession\_CanPreconfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_canpreconfig) or [OH\_CaptureSession\_CanPreconfigWithRatio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_canpreconfigwithratio) to check whether the current camera device supports a specific combination of **PreconfigType** and **PreconfigRatio**.

The resolution specifications vary according to the aspect ratio. For details, see the following table.

-   Preview output in normal photo mode
    
    | 
    Preconfiguration Type (PreconfigType)
    
     | 
    
    PRECONFIG\_RATIO\_1\_1
    
     | 
    
    PRECONFIG\_RATIO\_4\_3
    
     | 
    
    PRECONFIG\_RATIO\_16\_9
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    PRECONFIG\_720P
    
     | 
    
    720x720
    
     | 
    
    960x720
    
     | 
    
    1280x720
    
     |
    | 
    
    PRECONFIG\_1080P
    
     | 
    
    1080x1080
    
     | 
    
    1440x1080
    
     | 
    
    1920x1080
    
     |
    | 
    
    PRECONFIG\_4K
    
     | 
    
    1080x1080
    
     | 
    
    1440x1080
    
     | 
    
    1920x1080
    
     |
    | 
    
    PRECONFIG\_HIGH\_QUALITY
    
     | 
    
    1440x1440
    
     | 
    
    1920x1440
    
     | 
    
    2560x1440
    
     |
    
-   Photo output in normal photo mode
    
    | 
    Preconfiguration Type (PreconfigType)
    
     | 
    
    PRECONFIG\_RATIO\_1\_1
    
     | 
    
    PRECONFIG\_RATIO\_4\_3
    
     | 
    
    PRECONFIG\_RATIO\_16\_9
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    PRECONFIG\_720P
    
     | 
    
    720x720
    
     | 
    
    960x720
    
     | 
    
    1280x720
    
     |
    | 
    
    PRECONFIG\_1080P
    
     | 
    
    1080x1080
    
     | 
    
    1440x1080
    
     | 
    
    1920x1080
    
     |
    | 
    
    PRECONFIG\_4K
    
     | 
    
    2160x2160
    
     | 
    
    2880x2160
    
     | 
    
    3840x2160
    
     |
    | 
    
    PRECONFIG\_HIGH\_QUALITY
    
     | 
    
    Follows the maximum capability of the sensor
    
     | 
    
    Follows the maximum capability of the sensor
    
     | 
    
    Follows the maximum capability of the sensor
    
     |
    
-   Preview output in normal video mode
    
    | 
    Preconfiguration Type (PreconfigType)
    
     | 
    
    PRECONFIG\_RATIO\_1\_1
    
     | 
    
    PRECONFIG\_RATIO\_4\_3
    
     | 
    
    PRECONFIG\_RATIO\_16\_9
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    PRECONFIG\_720P
    
     | 
    
    720x720
    
     | 
    
    960x720
    
     | 
    
    1280x720
    
     |
    | 
    
    PRECONFIG\_1080P
    
     | 
    
    1080x1080
    
     | 
    
    1440x1080
    
     | 
    
    1920x1080
    
     |
    | 
    
    PRECONFIG\_4K
    
     | 
    
    1080x1080
    
     | 
    
    1440x1080
    
     | 
    
    1920x1080
    
     |
    | 
    
    PRECONFIG\_HIGH\_QUALITY
    
     | 
    
    1080x1080
    
     | 
    
    1440x1080
    
     | 
    
    1920x1080
    
     |
    
-   Video output in normal video mode
    
    | 
    Preconfiguration Type (PreconfigType)
    
     | 
    
    PRECONFIG\_RATIO\_1\_1
    
     | 
    
    PRECONFIG\_RATIO\_4\_3
    
     | 
    
    PRECONFIG\_RATIO\_16\_9
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    PRECONFIG\_720P
    
     | 
    
    720x720
    
     | 
    
    960x720
    
     | 
    
    1280x720
    
     |
    | 
    
    PRECONFIG\_1080P
    
     | 
    
    1080x1080
    
     | 
    
    1440x1080
    
     | 
    
    1920x1080
    
     |
    | 
    
    PRECONFIG\_4K
    
     | 
    
    2160x2160
    
     | 
    
    2880x2160
    
     | 
    
    3840x2160
    
     |
    | 
    
    PRECONFIG\_HIGH\_QUALITY
    
     | 
    
    2160x2160
    
     | 
    
    2880x2160
    
     | 
    
    3840x2160
    
     |
    
-   Photo output in normal video mode
    
    | 
    Preconfiguration Type (PreconfigType)
    
     | 
    
    PRECONFIG\_RATIO\_1\_1
    
     | 
    
    PRECONFIG\_RATIO\_4\_3
    
     | 
    
    PRECONFIG\_RATIO\_16\_9
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    PRECONFIG\_720P
    
     | 
    
    Follows the maximum capability of the sensor
    
     | 
    
    Follows the maximum capability of the sensor
    
     | 
    
    Follows the maximum capability of the sensor
    
     |
    | 
    
    PRECONFIG\_1080P
    
     | 
    
    Follows the maximum capability of the sensor
    
     | 
    
    Follows the maximum capability of the sensor
    
     | 
    
    Follows the maximum capability of the sensor
    
     |
    | 
    
    PRECONFIG\_4K
    
     | 
    
    Follows the maximum capability of the sensor
    
     | 
    
    Follows the maximum capability of the sensor
    
     | 
    
    Follows the maximum capability of the sensor
    
     |
    | 
    
    PRECONFIG\_HIGH\_QUALITY
    
     | 
    
    Follows the maximum capability of the sensor
    
     | 
    
    Follows the maximum capability of the sensor
    
     | 
    
    Follows the maximum capability of the sensor
    
     |
    

#### How to Develop

1.  Link the dynamic library in the CMake script.
    
    target\_link\_libraries(entry PUBLIC libohcamera.so libhilog\_ndk.z.so)
    
2.  Import the NDK APIs on the C++ side, and perform photo capture based on the surface ID passed in.
    
    #include "hilog/log.h"
    #include "ohcamera/camera.h"
    #include "ohcamera/camera\_input.h"
    #include "ohcamera/capture\_session.h"
    #include "ohcamera/photo\_output.h"
    #include "ohcamera/preview\_output.h"
    #include "ohcamera/video\_output.h"
    #include "ohcamera/camera\_manager.h"
    class NDKCamera {
    public:
        NDKCamera(char \*previewId, char \*photoId);
    };
    
    void CaptureSessionOnFocusStateChange(Camera\_CaptureSession \*session, Camera\_FocusState focusState) {
        OH\_LOG\_INFO(LOG\_APP, "CaptureSessionOnFocusStateChange");
    }
    
    void CaptureSessionOnError(Camera\_CaptureSession \*session, Camera\_ErrorCode errorCode) {
        OH\_LOG\_INFO(LOG\_APP, "CaptureSessionOnError = %{public}d", errorCode);
    }
    
    CaptureSession\_Callbacks \*GetCaptureSessionRegister(void) {
        static CaptureSession\_Callbacks captureSessionCallbacks = {.onFocusStateChange = CaptureSessionOnFocusStateChange,
                                                                   .onError = CaptureSessionOnError};
        return &captureSessionCallbacks;
    }
    
    void PreviewOutputOnFrameStart(Camera\_PreviewOutput \*previewOutput) {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutputOnFrameStart");
    }
    
    void PreviewOutputOnFrameEnd(Camera\_PreviewOutput \*previewOutput, int32\_t frameCount) {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutputOnFrameEnd = %{public}d", frameCount);
    }
    
    void PreviewOutputOnError(Camera\_PreviewOutput \*previewOutput, Camera\_ErrorCode errorCode) {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutputOnError = %{public}d", errorCode);
    }
    
    PreviewOutput\_Callbacks \*GetPreviewOutputListener(void) {
        static PreviewOutput\_Callbacks previewOutputListener = {.onFrameStart = PreviewOutputOnFrameStart,
                                                                .onFrameEnd = PreviewOutputOnFrameEnd,
                                                                .onError = PreviewOutputOnError};
        return &previewOutputListener;
    }
    
    void OnCameraInputError(const Camera\_Input \*cameraInput, Camera\_ErrorCode errorCode) {
        OH\_LOG\_INFO(LOG\_APP, "OnCameraInput errorCode = %{public}d", errorCode);
    }
    
    CameraInput\_Callbacks \*GetCameraInputListener(void) {
        static CameraInput\_Callbacks cameraInputCallbacks = {.onError = OnCameraInputError};
        return &cameraInputCallbacks;
    }
    
    void CameraManagerStatusCallback(Camera\_Manager \*cameraManager, Camera\_StatusInfo \*status) {
        OH\_LOG\_INFO(LOG\_APP, "CameraManagerStatusCallback is called");
    }
    
    CameraManager\_Callbacks \*GetCameraManagerListener() {
        static CameraManager\_Callbacks cameraManagerListener = {.onCameraStatus = CameraManagerStatusCallback};
        return &cameraManagerListener;
    }
    
    NDKCamera::NDKCamera(char \*previewId, char \*photoId) {
        Camera\_Manager \*cameraManager = nullptr;
        Camera\_Device \*cameras = nullptr;
        Camera\_CaptureSession \*captureSession = nullptr;
        Camera\_PreviewOutput \*previewOutput = nullptr;
        Camera\_PhotoOutput \*photoOutput = nullptr;
        Camera\_Input \*cameraInput = nullptr;
        uint32\_t size = 0;
        uint32\_t cameraDeviceIndex = 0;
        char \*previewSurfaceId = previewId;
        char \*photoSurfaceId = photoId;
        // Create a CameraManager object.
        Camera\_ErrorCode ret = OH\_Camera\_GetCameraManager(&cameraManager);
        if (cameraManager == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_Camera\_GetCameraMananger failed.");
        }
        // Listen for camera status changes.
        ret = OH\_CameraManager\_RegisterCallback(cameraManager, GetCameraManagerListener());
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_RegisterCallback failed.");
        }
    
        // Obtain the camera list.
        ret = OH\_CameraManager\_GetSupportedCameras(cameraManager, &cameras, &size);
        if (cameras == nullptr || size < 0 || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedCameras failed.");
        }
    
        // Create a camera input stream.
        ret = OH\_CameraManager\_CreateCameraInput(cameraManager, &cameras\[cameraDeviceIndex\], &cameraInput);
        if (cameraInput == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateCameraInput failed.");
        }
    
        // Listen for camera input errors.
        ret = OH\_CameraInput\_RegisterCallback(cameraInput, GetCameraInputListener());
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraInput\_RegisterCallback failed.");
        }
    
        // Open the camera.
        ret = OH\_CameraInput\_Open(cameraInput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraInput\_Open failed.");
        }
    
        // Create a session.
        ret = OH\_CameraManager\_CreateCaptureSession(cameraManager, &captureSession);
        if (captureSession == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateCaptureSession failed.");
        }
    
        // Listen for session errors.
        ret = OH\_CaptureSession\_RegisterCallback(captureSession, GetCaptureSessionRegister());
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_RegisterCallback failed.");
        }
    
        // Query the preconfig capability.
        bool canPreconfigResult = false;
        ret = OH\_CaptureSession\_CanPreconfig(captureSession, PRECONFIG\_1080P, &canPreconfigResult);
        if (ret != CAMERA\_OK || !canPreconfigResult) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_CanPreconfig failed.");
        }
    
        // Configure the preconfig feature.
        ret = OH\_CaptureSession\_Preconfig(captureSession, PRECONFIG\_1080P);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Preconfig failed.");
        }
    
        // Create a preview output stream, with the previewSurfaceId parameter set to the ID of the surface provided by the XComponent.
        ret = OH\_CameraManager\_CreatePreviewOutputUsedInPreconfig(cameraManager, previewSurfaceId, &previewOutput);
        if (previewOutput == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreatePreviewOutput failed.");
        }
    
        // Listen for preview output errors.
        ret = OH\_PreviewOutput\_RegisterCallback(previewOutput, GetPreviewOutputListener());
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PreviewOutput\_RegisterCallback failed.");
        }
    
        // Create a photo output stream, with the photoSurfaceId parameter set to the ID of the surface obtained through ImageReceiver.
        ret = OH\_CameraManager\_CreatePhotoOutputUsedInPreconfig(cameraManager, photoSurfaceId, &photoOutput);
        if (photoOutput == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreatePhotoOutput failed.");
        }
    
        // Start configuration for the session.
        ret = OH\_CaptureSession\_BeginConfig(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_BeginConfig failed.");
        }
    
        // Add the camera input stream to the session.
        ret = OH\_CaptureSession\_AddInput(captureSession, cameraInput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddInput failed.");
        }
    
        // Add the preview output stream to the session.
        ret = OH\_CaptureSession\_AddPreviewOutput(captureSession, previewOutput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPreviewOutput failed.");
        }
    
        // Add the photo output stream to the session.
        ret = OH\_CaptureSession\_AddPhotoOutput(captureSession, photoOutput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPhotoOutput failed.");
        }
    
        // Commit the session configuration.
        ret = OH\_CaptureSession\_CommitConfig(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_CommitConfig failed.");
        }
    
        // Start the session.
        ret = OH\_CaptureSession\_Start(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Start failed.");
        }
    
        // Check whether the camera has flash.
        Camera\_FlashMode flashMode = FLASH\_MODE\_AUTO;
        bool hasFlash = false;
        ret = OH\_CaptureSession\_HasFlash(captureSession, &hasFlash);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_HasFlash failed.");
        }
        if (hasFlash) {
            OH\_LOG\_INFO(LOG\_APP, "hasFlash success");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "hasFlash fail");
        }
        // Check whether a flash mode is supported.
        bool isSupported = false;
        ret = OH\_CaptureSession\_IsFlashModeSupported(captureSession, flashMode, &isSupported);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_IsFlashModeSupported failed.");
        }
        if (isSupported) {
            OH\_LOG\_INFO(LOG\_APP, "isFlashModeSupported success");
            // Set the flash mode.
            ret = OH\_CaptureSession\_SetFlashMode(captureSession, flashMode);
            if (ret == CAMERA\_OK) {
                OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_SetFlashMode success.");
            } else {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetFlashMode failed. %{public}d ", ret);
            }
            // Obtain the flash mode in use.
            ret = OH\_CaptureSession\_GetFlashMode(captureSession, &flashMode);
            if (ret == CAMERA\_OK) {
                OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetFlashMode success. flashMode: %{public}d ", flashMode);
            } else {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetFlashMode failed. %d ", ret);
            }
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "isFlashModeSupported fail");
        }
    
        // Check whether the continuous auto focus is supported.
        Camera\_FocusMode focusMode = FOCUS\_MODE\_CONTINUOUS\_AUTO;
        bool isFocusModeSupported = false;
        ret = OH\_CaptureSession\_IsFocusModeSupported(captureSession, focusMode, &isFocusModeSupported);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_IsFocusModeSupported failed.");
        }
        if (isFocusModeSupported) {
            OH\_LOG\_INFO(LOG\_APP, "isFocusModeSupported success");
            ret = OH\_CaptureSession\_SetFocusMode(captureSession, focusMode);
            if (ret != CAMERA\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetFocusMode failed. %{public}d ", ret);
            }
            ret = OH\_CaptureSession\_GetFocusMode(captureSession, &focusMode);
            if (ret == CAMERA\_OK) {
                OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetFocusMode success. focusMode%{public}d ", focusMode);
            } else {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetFocusMode failed. %d ", ret);
            }
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "isFocusModeSupported fail");
        }
    
        // Obtain the zoom ratio range supported by the camera.
        float minZoom;
        float maxZoom;
        ret = OH\_CaptureSession\_GetZoomRatioRange(captureSession, &minZoom, &maxZoom);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetZoomRatioRange failed.");
        } else {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetZoomRatioRange success. minZoom: %{public}f, maxZoom:%{public}f",
                        minZoom, maxZoom);
        }
        // Set a zoom ratio.
        ret = OH\_CaptureSession\_SetZoomRatio(captureSession, maxZoom);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_SetZoomRatio success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetZoomRatio failed. %{public}d ", ret);
        }
        // Obtain the zoom ratio of the camera.
        ret = OH\_CaptureSession\_GetZoomRatio(captureSession, &maxZoom);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetZoomRatio success. zoom: %{public}f ", maxZoom);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetZoomRatio failed. %{public}d ", ret);
        }
    
        // Take photos without photo capture settings.
        ret = OH\_PhotoOutput\_Capture(photoOutput);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_PhotoOutput\_Capture success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PhotoOutput\_Capture failed. %d ", ret);
        }
    
        // Stop the session.
        ret = OH\_CaptureSession\_Stop(captureSession);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_Stop success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Stop failed. %d ", ret);
        }
    
        // Release the camera input stream.
        ret = OH\_CameraInput\_Close(cameraInput);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CameraInput\_Close success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraInput\_Close failed. %d ", ret);
        }
    
        // Release the preview output stream.
        ret = OH\_PreviewOutput\_Release(previewOutput);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_PreviewOutput\_Release success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PreviewOutput\_Release failed. %d ", ret);
        }
    
        // Release the photo output stream.
        ret = OH\_PhotoOutput\_Release(photoOutput);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_PhotoOutput\_Release success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PhotoOutput\_Release failed. %d ", ret);
        }
    
        // Release the session.
        ret = OH\_CaptureSession\_Release(captureSession);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_Release success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Release failed. %d ", ret);
        }
    
        // Release the resources.
        ret = OH\_CameraManager\_DeleteSupportedCameras(cameraManager, cameras, size);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "Delete Cameras failed.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_DeleteSupportedCameras. ok");
        }
    
        ret = OH\_Camera\_DeleteCameraManager(cameraManager);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "Delete Cameras failed.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_Camera\_DeleteCameraManager. ok");
        }
    }
