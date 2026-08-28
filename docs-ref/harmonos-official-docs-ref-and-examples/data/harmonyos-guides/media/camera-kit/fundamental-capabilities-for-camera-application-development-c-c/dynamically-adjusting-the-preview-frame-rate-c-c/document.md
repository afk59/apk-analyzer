# Dynamically Adjusting the Preview Frame Rate (C/C++)

Dynamic frame rate adjustment is an important capability for managing the preview effect in live streaming and video applications. This capability allows applications to explicitly control the output frame rate to meet various service requirements at different frame rates.

In certain scenarios, reducing the frame rate can also help in conserving power when the camera is in use.

#### Constraints

The supported frame rate range and the frame rate setting are subject to the hardware's capabilities. Different hardware platforms may offer different default frame rates.

#### Development Process

Before using the preview functionality, create a camera session. After the session configuration is complete, the application must commit the configuration and start the session before using the camera functionalities.

The procedure is shown below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/yZwy6Mu7TqekPg3Dz1j5ow/en-us_image_0000002220860149.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB41F8AFEE95209ACA5B2CD85CFCE5ADFA1699AA356B6780A7456D06613D844E)

Pay attention to the differences (labeled with numbers in the figure above) between the dynamic adjustment of the preview frame rate and the standard [preview](../preview-c-c/document.md) process.

1.  When calling [OH\_CameraManager\_CreateCaptureSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcapturesession) to create a session, set the mode to **NORMAL\_PHOTO** or **NORMAL\_VIDEO**.
    
    The frame rate of the preview stream can be adjusted only when the session is in **NORMAL\_PHOTO** or **NORMAL\_VIDEO** mode. For details about the operation, see [Creating a Session and Specifying a Mode](#section10844102810218).
    
2.  The operation of [dynamically adjusting the frame rate](#section137971332201516) can be performed before or after preview is enabled.
3.  [Dynamic frame rate adjustment](#section137971332201516) is optional during preview. It involves the following operations:
    -   Query the supported frame rate range.
    -   Set a frame rate.
    -   Obtain the active frame rate.

For details about how to configure sessions and release resources, see [Session Management](../../mandatory-capabilities-for-camera-application-development-c-c/camera-session-management-c-c/document.md) and [Preview](../preview-c-c/document.md).

#### Importing Modules

1.  Import the NDK APIs.
    
     // Include the NDK header files.
     #include "hilog/log.h"
     #include "ohcamera/camera.h"
     #include "ohcamera/camera\_input.h"
     #include "ohcamera/capture\_session.h"
     #include "ohcamera/photo\_output.h"
     #include "ohcamera/preview\_output.h"
     #include "ohcamera/video\_output.h"
     #include "ohcamera/camera\_manager.h"
    
2.  Link the dynamic library in the CMake script.
    
     target\_link\_libraries(entry PUBLIC libohcamera.so libhilog\_ndk.z.so)
    

#### Creating a Session and Specifying a Mode

Before using preview and other functionalities, call [OH\_CameraManager\_CreateCaptureSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcapturesession) to create a camera session.

When creating the session, call [OH\_CaptureSession\_SetSessionMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setsessionmode) to set [Camera\_SceneMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_scenemode) to **NORMAL\_PHOTO** or **NORMAL\_VIDEO**. The created session is in photo capture or video recording mode.

The following creates a session in **NORMAL\_PHOTO** mode.

Camera\_ErrorCode CreateCaptureSession(Camera\_Manager \*cameraManager, Camera\_CaptureSession \*captureSession) {
   Camera\_ErrorCode ret = OH\_CameraManager\_CreateCaptureSession(cameraManager, &captureSession);
    if (captureSession == nullptr || ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateCaptureSession failed.");
    }
// Set the session mode to NORMAL\_PHOTO or NORMAL\_VIDEO. The following uses NORMAL\_PHOTO as an example.
    ret = OH\_CaptureSession\_SetSessionMode(captureSession, Camera\_SceneMode::NORMAL\_PHOTO);
    return ret;
}

#### Dynamically Adjusting the Frame Rate

1.  Call [OH\_PreviewOutput\_GetSupportedFrameRates](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_getsupportedframerates) to query the frame rate range supported by the current preview output.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/pyi4CQ2CSp2PmE7Yynv5rQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC1C4317EEF76E94173E30E5E7805537B3E0E4281C3AB14297C90609EAF39F61)
    
    **When to Call**:
    
    This operation must be performed after the session calls [OH\_CaptureSession\_CommitConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig) to complete stream configuration.
    
    **Restrictions on OH\_PreviewOutput\_GetSupportedFrameRates**:
    
    -   Once you have used **OH\_PreviewOutput\_GetSupportedFrameRates** to set a non-fixed frame rate, further calls to adjust the dynamic frame rate are not allowed.
    -   If you have set a fixed frame rate via **OH\_PreviewOutput\_GetSupportedFrameRates**, you may change it to another fixed rate. However, you must ensure the new rate is either a factor or a multiple of the previous one.
    
    Camera\_ErrorCode PreviewOutputGetSupportedFrameRates(Camera\_PreviewOutput\* previewOutput,
        Camera\_FrameRateRange\*\* frameRateRange, uint32\_t\* size) {
        Camera\_ErrorCode ret = OH\_PreviewOutput\_GetSupportedFrameRates(previewOutput, frameRateRange, size);
    
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PreviewOutput\_GetSupportedFrameRates failed.");
            return CAMERA\_INVALID\_ARGUMENT;
        }
        for (uint32\_t i = 0; i < \*size; i++) {
            OH\_LOG\_DEBUG(LOG\_APP, "PreviewOutputGetSupportedFrameRates: SupportedFrameRates min %{public}d", (\*frameRateRange)\[i\].min);
            OH\_LOG\_DEBUG(LOG\_APP, "PreviewOutputGetSupportedFrameRates: SupportedFrameRates max %{public}d", (\*frameRateRange)\[i\].max);
        }
        return ret;
    }
    
2.  Call [OH\_PreviewOutput\_SetFrameRate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_setframerate) to dynamically adjust the frame rate.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ezvM9KobQISvtcwiQeOfxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1682CE0C6E5A683CFA674F968E1B7DCCDDBEA155FF07BC0F9E42DB0FCADFE1A0)
    
    -   This operation must be performed after the session calls [OH\_CaptureSession\_CommitConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig) to complete stream configuration.
    -   It can be called at any time before or after the session calls [OH\_PreviewOutput\_Start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_start) to start preview.
    
    Camera\_ErrorCode PreviewOutputSetFrameRate(Camera\_PreviewOutput\* previewOutput,
        uint32\_t minFps, uint32\_t maxFps){
        Camera\_ErrorCode ret = OH\_PreviewOutput\_SetFrameRate(previewOutput, minFps, maxFps);
        if (ret != CAMERA\_OK) {
            return CAMERA\_INVALID\_ARGUMENT;
        }
        return ret;
    }
    
3.  (Optional) Call [OH\_PreviewOutput\_GetActiveFrameRate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_getactiveframerate) to query the frame rate that has been set and taken effect.
    
    The active frame rate can be obtained only when it is explicitly set by calling [OH\_PreviewOutput\_SetFrameRate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_setframerate).
    
    Camera\_ErrorCode PreviewOutputGetActiveFrameRate(Camera\_PreviewOutput\* previewOutput,
        Camera\_FrameRateRange\* frameRateRange){
        Camera\_ErrorCode ret = OH\_PreviewOutput\_GetActiveFrameRate(previewOutput, frameRateRange);
        if (ret != CAMERA\_OK) {
            return CAMERA\_INVALID\_ARGUMENT;
        }
        OH\_LOG\_DEBUG(LOG\_APP, "PreviewOutputGetActiveFrameRate: ActiveFrameRate frameRateRange\_ min %{public}d", (\*frameRateRange).min);
        OH\_LOG\_DEBUG(LOG\_APP, "PreviewOutputGetActiveFrameRate: ActiveFrameRate frameRateRange\_ max %{public}d", (\*frameRateRange).max);
        return ret;
    }
