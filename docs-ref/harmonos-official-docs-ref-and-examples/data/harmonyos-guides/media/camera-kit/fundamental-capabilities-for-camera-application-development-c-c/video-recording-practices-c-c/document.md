# Video Recording Practices (C/C++)

Before developing a camera application, you must [request required permissions](../../requesting-camera-development-permissions/document.md).

This topic provides sample code that covers the complete video recording process and the API calling sequence. For details about a single process (such as [device input management](../../mandatory-capabilities-for-camera-application-development-c-c/device-input-management-c-c/document.md), [session management](../../mandatory-capabilities-for-camera-application-development-c-c/camera-session-management-c-c/document.md), and [video recording](../video-recording-c-c/document.md)), see the corresponding sections.

#### Development Process

After obtaining the output stream capabilities supported by the camera, create a video stream. The development process is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/C-GeIEZ1Try4ozBxJqUPCA/en-us_image_0000002568684895.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56F2A313A9C73327E47392E44D876CE6D51B4EDCEB9A8BAE52BD2E5FF8666222)

#### Complete Sample Code

1.  Link the dynamic library in the CMake script.
    
    target\_link\_libraries(entry PUBLIC
        libace\_napi.z.so
        libohcamera.so
        libhilog\_ndk.z.so
    )
    
2.  Create the header file **ndk\_camera.h**.
    
    #include "ohcamera/camera.h"
    #include "ohcamera/camera\_input.h"
    #include "ohcamera/capture\_session.h"
    #include "ohcamera/photo\_output.h"
    #include "ohcamera/preview\_output.h"
    #include "ohcamera/video\_output.h"
    #include "ohcamera/camera\_manager.h"
    
    class NDKCamera {
    public:
        ~NDKCamera();
        NDKCamera(char\* previewId, char\* videoId);
    };
    
3.  Import the NDK APIs on the C++ side, and perform video recording based on the surface ID passed in.
    
    #include "hilog/log.h"
    #include <cmath>
    
    bool IsAspectRatioEqual(float videoAspectRatio, float previewAspectRatio)
    {
        float epsilon = 1e-6f;
        return fabsf(videoAspectRatio - previewAspectRatio) <= epsilon;
    }
    
    void OnCameraInputError(const Camera\_Input\* cameraInput, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "OnCameraInput errorCode = %{public}d", errorCode);
    }
    
    CameraInput\_Callbacks\* GetCameraInputListener(void)
    {
        static CameraInput\_Callbacks cameraInputCallbacks = {
            .onError = OnCameraInputError
        };
        return &cameraInputCallbacks;
    }
    
    void CaptureSessionOnFocusStateChange(Camera\_CaptureSession\* session, Camera\_FocusState focusState)
    {
        OH\_LOG\_INFO(LOG\_APP, "CaptureSessionOnFocusStateChange");
    }
    
    void CaptureSessionOnError(Camera\_CaptureSession\* session, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "CaptureSessionOnError = %{public}d", errorCode);
    }
    
    CaptureSession\_Callbacks\* GetCaptureSessionRegister(void)
    {
        static CaptureSession\_Callbacks captureSessionCallbacks = {
            .onFocusStateChange = CaptureSessionOnFocusStateChange,
            .onError = CaptureSessionOnError
        };
        return &captureSessionCallbacks;
    }
    
    void VideoOutputOnFrameStart(Camera\_VideoOutput\* videoOutput)
    {
        OH\_LOG\_INFO(LOG\_APP, "VideoOutputOnFrameStart");
    }
    
    void VideoOutputOnFrameEnd(Camera\_VideoOutput\* videoOutput, int32\_t frameCount)
    {
        OH\_LOG\_INFO(LOG\_APP, "VideoOutput frameCount = %{public}d", frameCount);
    }
    
    void VideoOutputOnError(Camera\_VideoOutput\* videoOutput, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "VideoOutput errorCode = %{public}d", errorCode);
    }
    
    VideoOutput\_Callbacks\* GetVideoOutputListener(void)
    {
        static VideoOutput\_Callbacks videoOutputListener = {
            .onFrameStart = VideoOutputOnFrameStart,
            .onFrameEnd = VideoOutputOnFrameEnd,
            .onError = VideoOutputOnError
        };
        return &videoOutputListener;
    }
    
    void CameraManagerStatusCallback(Camera\_Manager\* cameraManager, Camera\_StatusInfo\* status)
    {
        OH\_LOG\_INFO(LOG\_APP, "CameraManagerStatusCallback is called");
    }
    
    CameraManager\_Callbacks\* GetCameraManagerListener()
    {
        static CameraManager\_Callbacks cameraManagerListener = {
            .onCameraStatus = CameraManagerStatusCallback
        };
        return &cameraManagerListener;
    }
    
    NDKCamera::NDKCamera(char\* previewId, char\* videoId)
    {
        Camera\_Manager\* cameraManager = nullptr;
        Camera\_Device\* cameras = nullptr;
        Camera\_CaptureSession\* captureSession = nullptr;
        Camera\_OutputCapability\* cameraOutputCapability = nullptr;
        Camera\_VideoOutput\* videoOutput = nullptr;
        const Camera\_Profile\* previewProfile = nullptr;
        const Camera\_Profile\* photoProfile = nullptr;
        const Camera\_VideoProfile\* videoProfile = nullptr;
        Camera\_PreviewOutput\* previewOutput = nullptr;
        Camera\_PhotoOutput\* photoOutput = nullptr;
        Camera\_Input\* cameraInput = nullptr;
        uint32\_t size = 0;
        uint32\_t cameraDeviceIndex = 0;
        char\* videoSurfaceId = videoId;
        char\* previewSurfaceId = previewId;
        // Create a CameraManager object.
        Camera\_ErrorCode ret = OH\_Camera\_GetCameraManager(&cameraManager);
        if (cameraManager == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_Camera\_GetCameraManager failed.");
            return;
        }
        // Listen for camera status changes.
        ret = OH\_CameraManager\_RegisterCallback(cameraManager, GetCameraManagerListener());
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_RegisterCallback failed.");
            return;
        }
    
        // Obtain the camera list.
        ret = OH\_CameraManager\_GetSupportedCameras(cameraManager, &cameras, &size);
        if (cameras == nullptr || size <= 0 || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedCameras failed.");
            return;
        }
    
        for (int index = 0; index < size; index++) {
            OH\_LOG\_ERROR(LOG\_APP, "cameraId  =  %{public}s ", cameras\[index\].cameraId);              // Obtain the camera ID.
            OH\_LOG\_ERROR(LOG\_APP, "cameraPosition  =  %{public}d ", cameras\[index\].cameraPosition);  // Obtain the camera position.
            OH\_LOG\_ERROR(LOG\_APP, "cameraType  =  %{public}d ", cameras\[index\].cameraType);          // Obtain the camera type.
            OH\_LOG\_ERROR(LOG\_APP, "connectionType  =  %{public}d ", cameras\[index\].connectionType);  // Obtain the camera connection type.
        }
    
        if (size < cameraDeviceIndex + 1) {
            OH\_LOG\_ERROR(LOG\_APP, "cameraDeviceIndex is invalid.");
            return;
        }
    
        // Obtain the output stream capability supported by the camera.
        ret = OH\_CameraManager\_GetSupportedCameraOutputCapability(cameraManager, &cameras\[cameraDeviceIndex\],
                                                                &cameraOutputCapability);
        if (cameraOutputCapability == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedCameraOutputCapability failed.");
            return;
        }
    
        if (cameraOutputCapability->previewProfiles == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "previewProfiles == null");
            return;
        }
        previewProfile = cameraOutputCapability->previewProfiles\[0\];
        OH\_LOG\_INFO(LOG\_APP, "previewProfile width: %{public}d, height: %{public}d.", previewProfile->size.width,
            previewProfile->size.height);
        if (cameraOutputCapability->photoProfiles == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "photoProfiles == null");
            return;
        }
        photoProfile = cameraOutputCapability->photoProfiles\[0\];
    
        if (cameraOutputCapability->videoProfiles == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "videoProfiles == null");
            return;
        }
        // Ensure that the aspect ratio of the preview stream is the same as that of the video stream. To record HDR videos, choose Camera\_VideoProfile that supports HDR.
        Camera\_VideoProfile\*\* videoProfiles = cameraOutputCapability->videoProfiles;
        for (int index = 0; index < cameraOutputCapability->videoProfilesSize; index++) {
            bool isEqual = IsAspectRatioEqual((float)videoProfiles\[index\]->size.width / videoProfiles\[index\]->size.height,
                (float)previewProfile->size.width / previewProfile->size.height);
            // The profile of CAMERA\_FORMAT\_YUV\_420\_SP is used by default.
            if (isEqual && videoProfiles\[index\]->format == Camera\_Format::CAMERA\_FORMAT\_YUV\_420\_SP) {
                videoProfile = videoProfiles\[index\];
                OH\_LOG\_INFO(LOG\_APP, "videoProfile width: %{public}d, height: %{public}d.", videoProfile->size.width,
                    videoProfile->size.height);
                break;
            }
        }
        if (videoProfile == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "Get videoProfile failed.");
            return;
        }
        // Create a VideoOutput instance.
        ret = OH\_CameraManager\_CreateVideoOutput(cameraManager, videoProfile, videoSurfaceId, &videoOutput);
        if (videoOutput == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateVideoOutput failed.");
            return;
        }
    
        // Listen for video output errors.
        ret = OH\_VideoOutput\_RegisterCallback(videoOutput, GetVideoOutputListener());
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_VideoOutput\_RegisterCallback failed.");
        }
    
        // Create a session.
        ret = OH\_CameraManager\_CreateCaptureSession(cameraManager, &captureSession);
        if (captureSession == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateCaptureSession failed.");
            return;
        }
        // Listen for session errors.
        ret = OH\_CaptureSession\_RegisterCallback(captureSession, GetCaptureSessionRegister());
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_RegisterCallback failed.");
        }
    
        // Start configuration for the session.
        ret = OH\_CaptureSession\_BeginConfig(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_BeginConfig failed.");
            return;
        }
    
        // Create a camera input stream.
        ret = OH\_CameraManager\_CreateCameraInput(cameraManager, &cameras\[cameraDeviceIndex\], &cameraInput);
        if (cameraInput == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateCameraInput failed.");
            return;
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
            return;
        }
    
        // Add the camera input stream to the session.
        ret = OH\_CaptureSession\_AddInput(captureSession, cameraInput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddInput failed.");
            return;
        }
    
        // Create a preview output stream. For details about the surfaceId parameter, see the XComponent. The preview stream is the surface provided by the XComponent.
        ret = OH\_CameraManager\_CreatePreviewOutput(cameraManager, previewProfile, previewSurfaceId, &previewOutput);
        if (previewProfile == nullptr || previewOutput == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreatePreviewOutput failed.");
            return;
        }
    
        // Add the preview output stream to the session.
        ret = OH\_CaptureSession\_AddPreviewOutput(captureSession, previewOutput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPreviewOutput failed.");
            return;
        }
    
        // Add the video output stream to the session.
        ret = OH\_CaptureSession\_AddVideoOutput(captureSession, videoOutput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddVideoOutput failed.");
            return;
        }
    
        // Commit the session configuration.
        ret = OH\_CaptureSession\_CommitConfig(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_CommitConfig failed.");
            return;
        }
    
        // Start the session.
        ret = OH\_CaptureSession\_Start(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Start failed.");
            return;
        }
    
        // Start the video output stream.
        ret = OH\_VideoOutput\_Start(videoOutput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_VideoOutput\_Start failed.");
            return;
        }
    
        // Call avRecorder.start() on the TS side to start video recording.
    
        // Stop the video output stream.
        ret = OH\_VideoOutput\_Stop(videoOutput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_VideoOutput\_Stop failed.");
        }
    
        // Call avRecorder.stop() on the TS side to stop video recording.
    
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
    
        // Release the video output stream.
        ret = OH\_VideoOutput\_Release(videoOutput);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_VideoOutput\_Release success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_VideoOutput\_Release failed. %d ", ret);
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
        ret = OH\_CameraManager\_DeleteSupportedCameraOutputCapability(cameraManager, cameraOutputCapability);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "Delete Cameras failed.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_DeleteSupportedCameraOutputCapability success");
        }
        ret = OH\_Camera\_DeleteCameraManager(cameraManager);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "Delete Cameras failed.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_Camera\_DeleteCameraManager success");
        }
    }
