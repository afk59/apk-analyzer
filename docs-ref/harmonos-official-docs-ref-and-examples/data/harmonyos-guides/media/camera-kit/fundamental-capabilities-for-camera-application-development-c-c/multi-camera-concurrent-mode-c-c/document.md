# Multi-Camera Concurrent Mode (C/C++)

The multi-camera concurrent mode has been supported since API version 18, meaning an application can enable the front/rear cameras simultaneously for preview and video recording (the function of capturing photos with front/rear cameras simultaneously is not yet available).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/1jjO2sg2RymkEVK6LzUQYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85D2B5F0745B910F04B00BFA06EBE2E6D7B1BA71360F0F1221E674D3C7154F0D)

Operating both cameras at the same time imposes significant restrictions on available features. The current implementation supports seven core functions, as listed below. When using multi-camera concurrent mode, avoid accessing or enabling any capabilities beyond them.

1.  Flash
2.  Exposure
3.  Zoom
4.  Exposure compensation
5.  Focus
6.  Stabilization
7.  Color space

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera) for the API reference.

1.  Import the NDK, which provides camera-related properties and methods.
    
    #include <cstdint>
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
    #include "common/log\_common.h"
    
2.  Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(entry PUBLIC
       libohcamera.so
       libace\_napi.z.so
       libnative\_buffer.so
       libhilog\_ndk.z.so
       librawfile.z.so)
    
3.  Call [OH\_CameraManager\_GetCameraDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getcameradevice) to obtain the front and rear cameras. If the return value is **CAMERA\_SERVICE\_FATAL\_ERROR**, based on the configuration information in the sample, it indicates that the current device does not support the default type of camera for the specified position (front/rear), and the multi-camera concurrent mode cannot be enabled.
    
    void GetSupportedCameras(Camera\_Manager \*cameraManager)
    {
        Camera\_Device \*cameras;
        uint32\_t size = 0;
        Camera\_ErrorCode ret = OH\_CameraManager\_GetSupportedCameras(cameraManager, &cameras, &size);
        if (cameras == nullptr || &size == nullptr || ret != CAMERA\_OK) {
            return;
        }
    
        // Obtain the rear camera.
        ret = OH\_CameraManager\_GetCameraDevice(cameraManager, Camera\_Position::CAMERA\_POSITION\_BACK, Camera\_Type::CAMERA\_TYPE\_DEFAULT, &cameras\[0\]);
    
        // Obtain the front camera.
        ret = OH\_CameraManager\_GetCameraDevice(cameraManager, Camera\_Position::CAMERA\_POSITION\_FRONT, Camera\_Type::CAMERA\_TYPE\_DEFAULT, &cameras\[1\]);
    }
    
4.  Obtain the corresponding concurrent capability set. Obtain the [Camera\_ConcurrentInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-concurrentinfo) array through the [OH\_CameraManager\_GetCameraConcurrentInfos](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getcameraconcurrentinfos) method, which describes the supported modes and output capabilities for both the front and rear cameras when they are concurrently enabled in the specified multi‑camera concurrent mode. **The modes and output capabilities you configure must fall within the bounds of this concurrent capability set.**
    
    void GetSupportedOutputCapability(Camera\_Manager \*cameraManager, Camera\_Device \*cameras)
    {
        Camera\_ConcurrentInfo\* cameraConcurrentInfo;
        uint32\_t infoSize = 0;
        Camera\_ErrorCode ret = OH\_CameraManager\_GetCameraConcurrentInfos(cameraManager, cameras, 2, &cameraConcurrentInfo, &infoSize);
        if (cameraConcurrentInfo == nullptr || cameraConcurrentInfo->outputCapabilities == nullptr
            || cameraConcurrentInfo->outputCapabilities->previewProfiles == nullptr || ret != CAMERA\_OK) {
            return;
       }
    }
    
5.  Create a PreviewOutput object based on the concurrency capability set.
    
    void CreatePreviewOutput(Camera\_Manager \*cameraManager, Camera\_ConcurrentInfo\* cameraConcurrentInfo, char\* previewSurfaceId)
    {
        Camera\_Profile \*profile = cameraConcurrentInfo->outputCapabilities->previewProfiles\[0\];
        if (profile == nullptr) {
            return;
        }
        Camera\_PreviewOutput \*previewOutput;
        Camera\_ErrorCode ret = OH\_CameraManager\_CreatePreviewOutput(cameraManager, profile, previewSurfaceId, &previewOutput);
        if (previewOutput == nullptr || ret != CAMERA\_OK) {
            return;
        }
    }
    
6.  Open the camera. Call [OH\_CameraInput\_OpenConcurrentCameras](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-input-h#oh_camerainput_openconcurrentcameras) to open the specified camera in multi-camera concurrent mode. Before using this API, check whether the camera supports concurrent capabilities and call [OH\_CameraManager\_GetCameraConcurrentInfos](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getcameraconcurrentinfos) to obtain the concurrent capability set in the multi-camera concurrent mode. Do not use [OH\_CameraInput\_OpenConcurrentCameras](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-input-h#oh_camerainput_openconcurrentcameras) without querying the concurrency capability set, as this will result in camera opening failure.
    
    void CameraInputOpen(Camera\_Manager \*cameraManager, Camera\_Device \*cameras)
    {
        Camera\_Input \*cameraInput;
        Camera\_ErrorCode ret = OH\_CameraManager\_CreateCameraInput(cameraManager, &cameras\[0\], &cameraInput);
        if (cameraInput == nullptr || ret != CAMERA\_OK) {
            return;
        }
        // The current version supports opening the camera only in CAMERA\_CONCURRENT\_TYPE\_LIMITED\_CAPABILITY mode.
        ret = OH\_CameraInput\_OpenConcurrentCameras(cameraInput, Camera\_ConcurrentType::CAMERA\_CONCURRENT\_TYPE\_LIMITED\_CAPABILITY);
        if (ret != CAMERA\_OK) {
            return;
        }
    }
    
7.  Implement the session flow. Configure the corresponding camera input stream [Camera\_Input](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-input) and output stream. The following uses the preview output stream [Camera\_PreviewOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-previewoutput) as an example.
    
    void SessionFlowFn(Camera\_CaptureSession \*captureSession, Camera\_Input \*cameraInput, Camera\_PreviewOutput \*previewOutput)
    {
        // Start configuration for the session.
        Camera\_ErrorCode ret = OH\_CaptureSession\_BeginConfig(captureSession);
    
        // Add the camera input stream to the session.
        ret = OH\_CaptureSession\_AddInput(captureSession, cameraInput);
    
        // Add the preview output stream to the session.
        ret = OH\_CaptureSession\_AddPreviewOutput(captureSession, previewOutput);
     
        // Commit the configuration.
        ret = OH\_CaptureSession\_CommitConfig(captureSession);
    
        // Start the session.
        ret = OH\_CaptureSession\_Start(captureSession);
     
        return;
    }
    
8.  The following provides examples of configurable capabilities for front and rear cameras in multi-camera concurrent mode. (Currently, only the seven core functions listed at the beginning of this document are supported.)
    
    // Flash.
    void HasFlashFn(uint32\_t mode, Camera\_CaptureSession \*captureSession)
    {
        Camera\_FlashMode flashMode = static\_cast<Camera\_FlashMode>(mode);
        // Check whether the camera device has flash.
        bool hasFlash = false;
        Camera\_ErrorCode ret = OH\_CaptureSession\_HasFlash(captureSession, &hasFlash);
        if (captureSession == nullptr || ret != CAMERA\_OK || !hasFlash) {
            return;
        }
    
        // Check whether a flash mode is supported.
        bool isSupported = false;
       ret = OH\_CaptureSession\_IsFlashModeSupported(captureSession, flashMode, &isSupported);
        if (ret != CAMERA\_OK || !isSupported) {
            return;
        }
    
        // Set the flash mode.
        ret = OH\_CaptureSession\_SetFlashMode(captureSession, flashMode);
        if (ret != CAMERA\_OK) {
            return;
        }
    
        // Obtain the flash mode in use.
        ret = OH\_CaptureSession\_GetFlashMode(captureSession, &flashMode);
     }
    
    // Exposure
    void IsExposureModeSupportedFn(uint32\_t mode, Camera\_CaptureSession \*captureSession)
    {
        Camera\_ExposureMode exposureMode = static\_cast<Camera\_ExposureMode>(mode);
        bool isExposureModeSupported = false;
        Camera\_ErrorCode ret = OH\_CaptureSession\_IsExposureModeSupported(captureSession, exposureMode, &isExposureModeSupported);
        if (&isExposureModeSupported == nullptr || ret != CAMERA\_OK) {
            return;
        }
        ret = OH\_CaptureSession\_SetExposureMode(captureSession, exposureMode);
        if (ret != CAMERA\_OK) {
            return;
        }
        ret = OH\_CaptureSession\_GetExposureMode(captureSession, &exposureMode);
    }
