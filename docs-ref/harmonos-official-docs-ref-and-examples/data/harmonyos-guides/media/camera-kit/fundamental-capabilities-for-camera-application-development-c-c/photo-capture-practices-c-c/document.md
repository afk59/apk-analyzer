# Photo Capture Practices (C/C++)

Before developing a camera application, you must [request required permissions](../../requesting-camera-development-permissions/document.md).

This topic provides sample code that covers the complete photo capture process and the API calling sequence. For details about a single process (such as device input, session management, and photo capture), see the corresponding C/C++ development guide links provided in [Requesting Camera Development Permissions](../../mandatory-capabilities-for-camera-application-development-c-c/camera-device-management-c-c/document.md).

#### Development Process

After obtaining the output stream capabilities supported by the camera, create a photo stream. The development process is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/PH6jJvHRTEmHdmMUzq0-bA/en-us_image_0000002537925118.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAE79E7D59690893726153DDAE62C89449D429C35BAF018F37E9F7BD2CDD5776)

#### Complete Sample Code

1.  Link the dynamic library in the CMake script.
    
    target\_link\_libraries(entry PUBLIC
        libace\_napi.z.so
        libhilog\_ndk.z.so
        libnative\_buffer.so
        libohcamera.so
        libohimage.so
        libohfileuri.so
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
        NDKCamera(char\* previewId);
        Camera\_ErrorCode RegisterBufferCb(void\* cb);
    };
    
3.  Import the NDK APIs on the C++ side, and perform photo capture based on the surface ID passed in.
    
    #include "hilog/log.h"
    
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
    
    void PreviewOutputOnFrameStart(Camera\_PreviewOutput\* previewOutput)
    {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutputOnFrameStart");
    }
    
    void PreviewOutputOnFrameEnd(Camera\_PreviewOutput\* previewOutput, int32\_t frameCount)
    {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutputOnFrameEnd = %{public}d", frameCount);
    }
    
    void PreviewOutputOnError(Camera\_PreviewOutput\* previewOutput, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "PreviewOutputOnError = %{public}d", errorCode);
    }
    
    PreviewOutput\_Callbacks\* GetPreviewOutputListener(void)
    {
        static PreviewOutput\_Callbacks previewOutputListener = {
            .onFrameStart = PreviewOutputOnFrameStart,
            .onFrameEnd = PreviewOutputOnFrameEnd,
            .onError = PreviewOutputOnError
        };
        return &previewOutputListener;
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
    
    static void\* bufferCb = nullptr;
    Camera\_ErrorCode NDKCamera::RegisterBufferCb(void\* cb) {
        OH\_LOG\_INFO(LOG\_APP, " RegisterBufferCb start");
        if (cb == nullptr) {
            OH\_LOG\_INFO(LOG\_APP, " RegisterBufferCb invalid error");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        bufferCb = cb;
    
        return CAMERA\_OK;
    }
    void OnPhotoAvailable(Camera\_PhotoOutput\* photoOutput, OH\_PhotoNative\* photo) {
        OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable start!");
        OH\_ImageNative\* imageNative;
        Camera\_ErrorCode errCode = OH\_PhotoNative\_GetMainImage(photo, &imageNative);
        OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable errCode:%{public}d imageNative:%{public}p", errCode, imageNative);
        // Read the size attribute of OH\_ImageNative.
        Image\_Size size;
        Image\_ErrorCode imageErr = OH\_ImageNative\_GetImageSize(imageNative, &size);
        OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable imageErr:%{public}d width:%{public}d height:%{public}d", imageErr,
            size.width, size.height);
        // Read the number of elements in the component list of OH\_ImageNative.
        size\_t componentTypeSize = 0;
        imageErr = OH\_ImageNative\_GetComponentTypes(imageNative, nullptr, &componentTypeSize);
        OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable imageErr:%{public}d componentTypeSize:%{public}zu", imageErr,
            componentTypeSize);
        // Read the component list of OH\_ImageNative.
        uint32\_t\* components = new uint32\_t\[componentTypeSize\];
        imageErr = OH\_ImageNative\_GetComponentTypes(imageNative, &components, &componentTypeSize);
        OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable OH\_ImageNative\_GetComponentTypes imageErr:%{public}d", imageErr);
        // Read the buffer object corresponding to the first component of OH\_ImageNative.
        OH\_NativeBuffer\* nativeBuffer = nullptr;
        imageErr = OH\_ImageNative\_GetByteBuffer(imageNative, components\[0\], &nativeBuffer);
        OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable OH\_ImageNative\_GetByteBuffer imageErr:%{public}d", imageErr);
        // Read the size of the buffer corresponding to the first component of OH\_ImageNative.
        size\_t nativeBufferSize = 0;
        imageErr = OH\_ImageNative\_GetBufferSize(imageNative, components\[0\], &nativeBufferSize);
        OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable imageErr:%{public}d nativeBufferSize:%{public}zu", imageErr,
             nativeBufferSize);
        // Read the row stride corresponding to the first component of OH\_ImageNative.
        int32\_t rowStride = 0;
        imageErr = OH\_ImageNative\_GetRowStride(imageNative, components\[0\], &rowStride);
        OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable imageErr:%{public}d rowStride:%{public}d", imageErr, rowStride);
        // Read the pixel stride corresponding to the first component of OH\_ImageNative.
        int32\_t pixelStride = 0;
        imageErr = OH\_ImageNative\_GetPixelStride(imageNative, components\[0\], &pixelStride);
        OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable imageErr:%{public}d pixelStride:%{public}d", imageErr, pixelStride);
        // Map the ION memory to the process address space.
        void\* virAddr = nullptr; // Point to the virtual address of the mapped memory. After unmapping, the pointer is invalid.
        int32\_t ret = OH\_NativeBuffer\_Map(nativeBuffer, &virAddr); // After mapping, the start address of the memory is returned through the parameter virAddr.
        OH\_LOG\_INFO(LOG\_APP, "OnPhotoAvailable OH\_NativeBuffer\_Map err:%{public}d", ret);
        // Pass the processed buffer to the ArkTS side through the callback for image display or storage (using a security component). For details, see Photo Capture (C/C++).
        if (bufferCb == nullptr) {
            OH\_LOG\_INFO(LOG\_APP, "Current bufferCb invalid error");
            return;
        }
        auto cb = (void (\*)(void \*, size\_t))(bufferCb);
        cb(virAddr, nativeBufferSize);
        // After the processing is complete, unmap and release the buffer.
        ret = OH\_NativeBuffer\_Unmap(nativeBuffer);
        if (ret != 0) {
            OH\_LOG\_ERROR(LOG\_APP, "OnPhotoAvailable OH\_NativeBuffer\_Unmap error:%{public}d", ret);
        }
    }
    
    NDKCamera::NDKCamera(char\* previewId)
    {
        Camera\_Manager\* cameraManager = nullptr;
        Camera\_Device\* cameras = nullptr;
        Camera\_CaptureSession\* captureSession = nullptr;
        Camera\_OutputCapability\* cameraOutputCapability = nullptr;
        const Camera\_Profile\* previewProfile = nullptr;
        const Camera\_Profile\* photoProfile = nullptr;
        Camera\_PreviewOutput\* previewOutput = nullptr;
        Camera\_PhotoOutput\* photoOutput = nullptr;
        Camera\_Input\* cameraInput = nullptr;
        uint32\_t size = 0;
        uint32\_t cameraDeviceIndex = 0;
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
        }
    
        // Obtain the camera list.
        ret = OH\_CameraManager\_GetSupportedCameras(cameraManager, &cameras, &size);
        if (cameras == nullptr || size <= 0 || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedCameras failed.");
            return;
        }
    
        if (size < cameraDeviceIndex + 1) {
            OH\_LOG\_ERROR(LOG\_APP, "cameraDeviceIndex is invalid.");
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
            return;
        }
    
        // Open the camera.
        ret = OH\_CameraInput\_Open(cameraInput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraInput\_Open failed.");
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
        // Select an appropriate preview resolution from previewProfiles of cameraOutputCapability.
        previewProfile = cameraOutputCapability->previewProfiles\[0\];
    
        if (cameraOutputCapability->photoProfiles == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "photoProfiles == null");
            return;
        }
        // Select an appropriate photo resolution from photoProfiles of cameraOutputCapability.
        photoProfile = cameraOutputCapability->photoProfiles\[0\];
    
        // Create a preview output stream, with the previewSurfaceId parameter set to the ID of the surface provided by the XComponent.
        ret = OH\_CameraManager\_CreatePreviewOutput(cameraManager, previewProfile, previewSurfaceId, &previewOutput);
        if (previewProfile == nullptr || previewOutput == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreatePreviewOutput failed.");
            return;
        }
    
        // Listen for preview output errors.
        ret = OH\_PreviewOutput\_RegisterCallback(previewOutput, GetPreviewOutputListener());
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PreviewOutput\_RegisterCallback failed.");
        }
    
        // Create a photo output stream.
        ret = OH\_CameraManager\_CreatePhotoOutputWithoutSurface(cameraManager, photoProfile, &photoOutput);
    
        // Listen for the callback of one-time photo capture.
        ret = OH\_PhotoOutput\_RegisterPhotoAvailableCallback(photoOutput, OnPhotoAvailable);
    
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
    
        // Add the camera input stream to the session.
        ret = OH\_CaptureSession\_AddInput(captureSession, cameraInput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddInput failed.");
            return;
        }
    
        // Add the preview output stream to the session.
        ret = OH\_CaptureSession\_AddPreviewOutput(captureSession, previewOutput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPreviewOutput failed.");
            return;
        }
    
        // Add the photo output stream to the session.
        ret = OH\_CaptureSession\_AddPhotoOutput(captureSession, photoOutput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPhotoOutput failed.");
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
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetFlashMode failed. ret : %{public}d ", ret);
            }
    
            // Obtain the flash mode in use.
            ret = OH\_CaptureSession\_GetFlashMode(captureSession, &flashMode);
            if (ret == CAMERA\_OK) {
                OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetFlashMode success. flashMode: %{public}d ", flashMode);
            } else {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetFlashMode failed. ret : %{public}d ", ret);
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
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetFocusMode failed. ret : %{public}d ", ret);
            }
            ret = OH\_CaptureSession\_GetFocusMode(captureSession, &focusMode);
            if (ret == CAMERA\_OK) {
                OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetFocusMode success. focusMode%{public}d ", focusMode);
            } else {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetFocusMode failed. ret : %{public}d ", ret);
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
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetZoomRatio failed. ret : %{public}d ", ret);
        }
    
        // Obtain the zoom ratio of the camera.
        ret = OH\_CaptureSession\_GetZoomRatio(captureSession, &maxZoom);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_GetZoomRatio success. zoom: %{public}f ", maxZoom);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_GetZoomRatio failed. ret : %{public}d ", ret);
        }
    
        // Take photos without photo capture settings.
        ret = OH\_PhotoOutput\_Capture(photoOutput);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_PhotoOutput\_Capture success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PhotoOutput\_Capture failed. ret : %{public}d ", ret);
        }
    
        // Stop the session.
        ret = OH\_CaptureSession\_Stop(captureSession);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_Stop success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Stop failed. ret : %{public}d ", ret);
        }
    
        // Release the camera input stream.
        ret = OH\_CameraInput\_Close(cameraInput);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CameraInput\_Close success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraInput\_Close failed. ret : %{public}d ", ret);
        }
    
        // Release the preview output stream.
        ret = OH\_PreviewOutput\_Release(previewOutput);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_PreviewOutput\_Release success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PreviewOutput\_Release failed. ret : %{public}d ", ret);
        }
    
        // Release the photo output stream.
        ret = OH\_PhotoOutput\_Release(photoOutput);
        if (ret == CAMERA\_OK) {
          OH\_LOG\_INFO(LOG\_APP, "OH\_PhotoOutput\_Release success ");
        } else {
          OH\_LOG\_ERROR(LOG\_APP, "OH\_PhotoOutput\_Release failed. ret : %{public}d ", ret);
        }
    
        // Release the session.
        ret = OH\_CaptureSession\_Release(captureSession);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_Release success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Release failed. ret : %{public}d ", ret);
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
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_DeleteSupportedCameraOutputCapability. ok");
        }
        ret = OH\_Camera\_DeleteCameraManager(cameraManager);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "Delete Cameras failed.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_Camera\_DeleteCameraManager. ok");
        }
    }
