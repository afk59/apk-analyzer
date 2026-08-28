# Focus (C/C++)

The camera framework offers capabilities for focusing, enabling applications to configure focus modes and focus points based on specific use cases.

#### How to Develop

For details about the APIs, see [Camera API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h).

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
    
3.  Call [OH\_CaptureSession\_SetFocusMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setfocusmode) to set a focus mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/A1yZ8UZVSq--MP15tdTncA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19C7744A4B0ECE78D8041EC3515AB026F095273B8858C319E7699DDD7A9612E3)
    
    -   Prior to this operation, call [OH\_CaptureSession\_IsFocusModeSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_isfocusmodesupported) to check whether the device supports the specified focus mode.
    -   This operation must be performed after the session calls [OH\_CaptureSession\_CommitConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig) to complete stream configuration.
    
     Camera\_ErrorCode SetFocusMode(Camera\_CaptureSession \*captureSession, uint32\_t mode)
     {
         bool isFocusModeSupported = false;
         Camera\_FocusMode focusMode = static\_cast<Camera\_FocusMode>(mode);
         Camera\_ErrorCode ret = OH\_CaptureSession\_IsFocusModeSupported(captureSession, focusMode, &isFocusModeSupported);
         if (&isFocusModeSupported == nullptr || ret != CAMERA\_OK) {
             OH\_LOG\_ERROR(LOG\_APP, "IsFocusModeSupported failed.");
             return CAMERA\_INVALID\_ARGUMENT;
         }
    
         if (!isFocusModeSupported) {
             OH\_LOG\_INFO(LOG\_APP, "current focusMode(%{public}d) is not supported.", focusMode);
             return CAMERA\_OK;
         }
    
         OH\_LOG\_INFO(LOG\_APP, "OH\_CaptureSession\_SetFocusMode focusMode(%{public}d).", focusMode);
         ret = OH\_CaptureSession\_SetFocusMode(captureSession, focusMode);
         if (ret != CAMERA\_OK) {
             OH\_LOG\_ERROR(LOG\_APP, "SetFocusMode failed.");
             return CAMERA\_INVALID\_ARGUMENT;
         }
         return ret;
     }
    
4.  If the focus mode is set to autofocus by using [OH\_CaptureSession\_SetFocusMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setfocusmode), call [OH\_CaptureSession\_SetFocusPoint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setfocuspoint) to set the focus point. The camera triggers autofocus based on the focus point.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/bHtjrR5GRuq89l1RLlLRaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BE5D5EA39726F0E9878BED1B33F2FE8761FEB2139B4058229DC1BFC38377A6E)
    
    This operation must be performed after the session calls [OH\_CaptureSession\_CommitConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig) to complete stream configuration.
    
     Camera\_ErrorCode SetFocusPoint(Camera\_CaptureSession \*captureSession, float x, float y)
     {
         Camera\_Point focusPoint;
         focusPoint.x = x;
         focusPoint.y = y;
         Camera\_ErrorCode ret = OH\_CaptureSession\_SetFocusPoint(captureSession, focusPoint);
         if (ret != CAMERA\_OK) {
             OH\_LOG\_ERROR(LOG\_APP, "SetFocusPoint failed.");
             return CAMERA\_INVALID\_ARGUMENT;
         }
         return ret;
     }
    

#### Status Listening

During camera application development, you can listen for camera focus status changes at any time.

Obtain the listening result by registering the callback function of [OnFocusStateChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_onfocusstatechange). This event is triggered only when the camera focus status changes in autofocus mode.

void CaptureSessionOnFocusStateChange(Camera\_CaptureSession\* captureSession, Camera\_FocusState focusState)
    {
        OH\_LOG\_INFO(LOG\_APP, "CaptureSession\_Callbacks CaptureSessionOnFocusStateChange");
        OH\_LOG\_INFO(LOG\_APP, "CaptureSession focusState = %{public}d", focusState);
        // To ensure user experience, you can set the focus mode to continuous autofocus after autofocus is successful.
        if (focusState == Camera\_FocusState::FOCUS\_STATE\_FOCUSED) {
            Camera\_ErrorCode ret = SetFocusMode(captureSession, Camera\_FocusMode::FOCUS\_MODE\_CONTINUOUS\_AUTO);
        }
    }

    void CaptureSessionOnError(Camera\_CaptureSession\* captureSession, Camera\_ErrorCode errorCode)
    {
        OH\_LOG\_INFO(LOG\_APP, "CaptureSession\_Callbacks CaptureSessionOnError");
        OH\_LOG\_INFO(LOG\_APP, "CaptureSession errorCode = %{public}d", errorCode);
    }

    CaptureSession\_Callbacks\* GetCaptureSessionRegister(void)
    {
        static CaptureSession\_Callbacks captureSessionCallbacks = {
            .onFocusStateChange = CaptureSessionOnFocusStateChange,
            .onError = CaptureSessionOnError
        };
        return &captureSessionCallbacks;
    }

Camera\_ErrorCode RegisterCallback(Camera\_CaptureSession\* captureSession)
{
    Camera\_ErrorCode ret = OH\_CaptureSession\_RegisterCallback(captureSession, GetCaptureSessionRegister());
    if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_CaptureSession\_RegisterCallback failed.");
    }
    return ret;
}
