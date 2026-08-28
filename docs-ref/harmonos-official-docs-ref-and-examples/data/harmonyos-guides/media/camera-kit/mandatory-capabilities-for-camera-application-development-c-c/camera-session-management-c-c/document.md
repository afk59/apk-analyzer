# Camera Session Management (C/C++)

Before using the camera application for preview, photo capture, video recording, and metadata management, you must create a camera session.

You can implement the following functions in the session:

-   Configure the camera input and output streams. This is mandatory for photo capture.
    
    Configuring an input stream is to add a device input, which means that the user selects a camera for photo capture. Configuring an output stream is to select a data output mode. For example, to implement photo capture, you must configure both the preview stream and photo stream as the output stream. The data of the preview stream is displayed on the **XComponent**, and that of the photo stream is saved to the Gallery application through the ImageReceiver API.
    
-   Perform more operations on the camera device. For example, add the flash and adjust the focal length. For details about the supported configurations and APIs, see [Camera API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera).
    
-   Control session switching. The application can switch the camera mode by removing and adding output streams. For example, to switch from photo capture to video recording, the application must remove the photo output stream and add the video output stream.
    

After the session configuration is complete, the application must commit the configuration and start the session before using the camera functionalities.

#### How to Develop

1.  Import the NDK.
    
    #include "hilog/log.h"
    #include "ohcamera/camera.h"
    #include "ohcamera/camera\_input.h"
    #include "ohcamera/capture\_session.h"
    #include "ohcamera/photo\_output.h"
    #include "ohcamera/preview\_output.h"
    #include "ohcamera/video\_output.h"
    #include "ohcamera/camera\_manager.h"
    
2.  Link the dynamic library in the CMake script.
    
    target\_link\_libraries(entry PUBLIC
        libace\_napi.z.so
        libohcamera.so
        libhilog\_ndk.z.so
    )
    
3.  Call [OH\_CameraManager\_CreateCaptureSession()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcapturesession) to create a session.
    
    Camera\_CaptureSession\* CreateCaptureSession(Camera\_Manager\* cameraManager)
    {
        Camera\_CaptureSession\* captureSession = nullptr;
        if (cameraManager == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "cameraManager is nullptr.");
            return captureSession;
        }
        Camera\_ErrorCode ret = OH\_CameraManager\_CreateCaptureSession(cameraManager, &captureSession);
        if (captureSession == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateCaptureSession failed.");
        }
        return captureSession;
    }
    
4.  Call [OH\_CaptureSession\_SetSessionMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setsessionmode) to set the session mode.
    
    Camera\_ErrorCode SetSessionMode(Camera\_CaptureSession\* captureSession)
    {
        Camera\_ErrorCode ret = OH\_CaptureSession\_SetSessionMode(captureSession, NORMAL\_VIDEO);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_SetSessionMode failed.");
        }
        return ret;
    }
    
5.  Call [OH\_CaptureSession\_BeginConfig()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_beginconfig) to configure the session.
    
    Camera\_ErrorCode BeginConfig(Camera\_CaptureSession\* captureSession)
    {
        Camera\_ErrorCode ret = OH\_CaptureSession\_BeginConfig(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_BeginConfig failed.");
        }
        return ret;
    }
    
6.  Configure the session. You can call [OH\_CaptureSession\_AddInput()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_addinput) to add an input stream to the session, and call [OH\_CaptureSession\_AddPreviewOutput()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_addpreviewoutput) and [OH\_CaptureSession\_AddPhotoOutput()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_addphotooutput) to add output streams to the session. The code snippet below uses adding the preview stream **previewOutput** and photo stream **photoOutput** as an example to implement the photo capture and preview mode.
    
    After the configuration, call [OH\_CaptureSession\_CommitConfig()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig) and [OH\_CaptureSession\_Start()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_start) to commit the configuration and start the session.
    
    Camera\_ErrorCode StartSession(Camera\_CaptureSession\* captureSession, Camera\_Input\* cameraInput,
        Camera\_PreviewOutput\* previewOutput, Camera\_PhotoOutput\* photoOutput)
    {
        // Add the camera input stream to the session.
        Camera\_ErrorCode ret = OH\_CaptureSession\_AddInput(captureSession, cameraInput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddInput failed.");
            return ret;
        }
    
        // Add the preview output stream to the session.
        ret = OH\_CaptureSession\_AddPreviewOutput(captureSession, previewOutput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPreviewOutput failed.");
            return ret;
        }
    
        // Add the photo output stream to the session.
        ret = OH\_CaptureSession\_AddPhotoOutput(captureSession, photoOutput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddPhotoOutput failed.");
            return ret;
        }
    
        // Commit the session configuration.
        ret = OH\_CaptureSession\_CommitConfig(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_CommitConfig failed.");
            return ret;
        }
    
        // Start the session.
        ret = OH\_CaptureSession\_Start(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Start failed.");
        }
        return ret;
    }
    
7.  Control the session. You can call [OH\_CaptureSession\_Stop()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_stop) to stop the session, and call [OH\_CaptureSession\_RemovePhotoOutput()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_removephotooutput) and [OH\_CaptureSession\_AddVideoOutput()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_addvideooutput) to switch to another session. The code snippet below uses removing the photo stream **photoOutput** and adding the video stream **videoOutput** as an example to complete the switching from photo capture to video recording.
    
    Camera\_ErrorCode ReloadSession(Camera\_CaptureSession\* captureSession, Camera\_PhotoOutput\* photoOutput,
        Camera\_VideoOutput\* videoOutput)
    {
        Camera\_ErrorCode ret = OH\_CaptureSession\_Stop(captureSession);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_Stop success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Stop failed. %d ", ret);
        }
        ret = OH\_CaptureSession\_BeginConfig(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_BeginConfig failed.");
            return ret;
        }
        // Remove the photo output stream from the session.
        ret = OH\_CaptureSession\_RemovePhotoOutput(captureSession, photoOutput);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_RemovePhotoOutput success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_RemovePhotoOutput failed. %d ", ret);
        }
        // Release the photoOutput instance.
        ret = OH\_PhotoOutput\_Release(photoOutput);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_PhotoOutput\_Release success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PhotoOutput\_Release failed. %d ", ret);
        }
        // Add the video output stream to the session.
        ret = OH\_CaptureSession\_AddVideoOutput(captureSession, videoOutput);
        if (ret == CAMERA\_OK) {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_AddVideoOutput success ");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_AddVideoOutput failed. %d ", ret);
            return ret;
        }
        // Commit the session configuration.
        ret = OH\_CaptureSession\_CommitConfig(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_CommitConfig failed.");
            return ret;
        }
    
        // Start the session.
        ret = OH\_CaptureSession\_Start(captureSession);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_Start failed.");
        }
        return ret;
    }
