# Camera Metadata (C/C++)

Metadata is the description and context of image information returned by the camera application. It provides detailed data for the image information, such as the coordinates of a viewfinder frame for identifying a portrait in a photo or video.

Metadata uses a tag (key) to find the corresponding data (value) during the transfer of parameters and configurations, reducing memory copy operations.

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
    
2.  Link the dynamic library in the CMake script.
    
    target\_link\_libraries(entry PUBLIC
        libace\_napi.z.so
        libohcamera.so
        libhilog\_ndk.z.so
    )
    
3.  Call **OH\_CameraManager\_GetSupportedCameraOutputCapability()** to obtain the metadata types supported by the current device, and then call **OH\_CameraManager\_CreateMetadataOutput()** to create a metadata output stream.
    
    Camera\_ErrorCode NDKCamera::CreateMetadataOutput(void)
    {
        metaDataObjectType\_ = cameraOutputCapability\_->supportedMetadataObjectTypes\[0\];
        if (metaDataObjectType\_ == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "Get metaDataObjectType failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        ret\_ = OH\_CameraManager\_CreateMetadataOutput(cameraManager\_, metaDataObjectType\_, &metadataOutput\_);
        if (metadataOutput\_ == nullptr || ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "CreateMetadataOutput failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        MetadataOutputRegisterCallback();
        return ret\_;
    }
    
4.  Call [OH\_CameraManager\_CreateCaptureSession()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcapturesession) to create a session.
    
    ret = OH\_CameraManager\_CreateCaptureSession(cameraManager\_, &captureSession\_);
    if (captureSession\_ == nullptr || ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Create captureSession failed.");
    }
    
5.  Configure the session. After the configuration, call [OH\_CaptureSession\_Start()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_start) to output metadata. If the call fails, an error code is returned. For details about the error code types, see [Camera\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_errorcode).
    
    // Start configuration for the session.
    Camera\_ErrorCode ret = OH\_CaptureSession\_BeginConfig(captureSession\_);
    
    // Add the camera input stream to the session.
    ret = OH\_CaptureSession\_AddInput(captureSession\_, cameraInput\_);
    
    // Add the camera preview stream to the session.
    ret = OH\_CaptureSession\_AddPreviewOutput(captureSession\_, previewOutput\_);
    
    if (isVideo\_) {
        // Add the camera recording stream to the session.
        AddVideoOutput();
        if (isHdrVideo) {
            // Set the color space to OH\_COLORSPACE\_BT2020\_HLG\_LIMIT for HDR Vivid videos.
            OH\_NativeBuffer\_ColorSpace colorSpace = OH\_NativeBuffer\_ColorSpace::OH\_COLORSPACE\_BT2020\_HLG\_LIMIT;
            SetColorSpace(colorSpace);
        }
    } else {
        // Add the photo capture stream to the session.
        AddPhotoOutput();
        ret = CreateMetadataOutput();
        ret = OH\_CaptureSession\_AddMetadataOutput(captureSession\_, metadataOutput\_);
        OH\_NativeBuffer\_ColorSpace colorSpace = OH\_NativeBuffer\_ColorSpace::OH\_COLORSPACE\_P3\_FULL;
        SetColorSpace(colorSpace);
    }
    
    // Submit the session configuration.
    ret = OH\_CaptureSession\_CommitConfig(captureSession\_);
    // ...
    
    InitPreviewRotation();
    // Start the session.
    OH\_LOG\_INFO(LOG\_APP, "session start");
    ret = OH\_CaptureSession\_Start(captureSession\_);
    
6.  Call **stop()** to stop outputting metadata. If the call fails, an error code is returned.
    
    Camera\_ErrorCode StopMetadataOutput(Camera\_MetadataOutput\* metadataOutput)
    {
        Camera\_ErrorCode ret = OH\_MetadataOutput\_Stop(metadataOutput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_MetadataOutput\_Stop failed.");
        }
        return ret;
    }
    

#### Status Listening

During camera application development, you can listen for the status of metadata objects and output stream.

-   Register the **'metadataObjectsAvailable'** event to listen for metadata objects that are available. When a valid metadata object is detected, the callback function returns the metadata. This event can be registered when a MetadataOutput object is created.
    
    void OnMetadataObjectAvailable(Camera\_MetadataOutput \*metadataOutput, Camera\_MetadataObject \*metadataObject,
        uint32\_t size)
    {
        OH\_LOG\_INFO(LOG\_APP, "size = %{public}d", size);
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/daQDZKYtTRe73ZpuqxsPww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67426B326F3D50D1388F5CCF01D938359AF8183FB1E695D61DF0DCF01E89BD0B)
    
    Currently, only **FACE\_DETECTION** is available for the metadata type. The metadata object is the rectangle of the recognized face, including the x-axis coordinate and y-axis coordinate of the top-left corner of the rectangle as well as the width and height of the rectangle.
    
-   Register the **'error'** event to listen for metadata stream errors. The callback function returns an error code when an API is incorrectly used. For details about the error code types, see [Camera\_ErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_errorcode).
    
    void OnMetadataOutputError(Camera\_MetadataOutput \*metadataOutput, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "OnMetadataOutput errorCode = %{public}d", errorCode);
    }
    
    MetadataOutput\_Callbacks \*NDKCamera::GetMetadataOutputListener(void)
    {
        static MetadataOutput\_Callbacks metadataOutputListener = {
            .onMetadataObjectAvailable = OnMetadataObjectAvailable,
            .onError = OnMetadataOutputError
        };
        return &metadataOutputListener;
    }
    
    Camera\_ErrorCode NDKCamera::MetadataOutputRegisterCallback(void)
    {
        ret\_ = OH\_MetadataOutput\_RegisterCallback(metadataOutput\_, GetMetadataOutputListener());
        if (ret\_ != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_MetadataOutput\_RegisterCallback failed.");
        }
        return ret\_;
    }
