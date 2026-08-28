# Using the Flashlight (C++)

To use the flashlight mode, you manipulate your device to turn on the flashlight, which then stays on persistently.

When you use the flashlight mode with a camera application, the following situations may occur:

-   When the rear camera is used and [Camera\_FlashMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_flashmode) is set to **off**, the flashlight cannot be turned on.
-   When the front camera is used, the flashlight can be turned on and remains steady on.
-   When you switch from the front camera to the rear camera, the flashlight will be automatically turned off if it was turned on previously.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera) for the API reference.

1.  Import the NDK.
    
    // Include the NDK header files.
    #include "hilog/log.h"
    #include "ohcamera/camera.h"
    #include "ohcamera/camera\_input.h"
    #include "ohcamera/capture\_session.h"
    #include "ohcamera/camera\_manager.h"
    
2.  Link the dynamic library in the CMake script.
    
    target\_link\_libraries(entry PUBLIC
        libace\_napi.z.so
        libohcamera.so
        libhilog\_ndk.z.so
    )
    
3.  Call [OH\_CameraManager\_IsTorchSupported()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_istorchsupported) to check whether the current device supports the flashlight.
    
    bool IsTorchSupported(Camera\_Manager\* cameraManager)
    {
        // Check whether the device supports the flashlight.
        bool isTorchSupported = false;
        if (cameraManager == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "cameraManager is nullptr.");
            return isTorchSupported;
        }
        Camera\_ErrorCode ret = OH\_CameraManager\_IsTorchSupported(cameraManager, &isTorchSupported);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_IsTorchSupported failed.");
        }
        if (isTorchSupported) {
            OH\_LOG\_INFO(LOG\_APP, "isTorchSupported success.");
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "isTorchSupported failed.");
        }
        return isTorchSupported;
    }
    
4.  Call [OH\_CameraManager\_IsTorchSupportedByTorchMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_istorchsupportedbytorchmode) to check whether the current device supports a specific flashlight mode.
    
    bool IsTorchSupportedByTorchMode(Camera\_Manager\* cameraManager, Camera\_TorchMode torchMode)
    {
        bool torchModeSupported = false;
        Camera\_ErrorCode ret = OH\_CameraManager\_IsTorchSupportedByTorchMode(cameraManager, torchMode, &torchModeSupported);
        if (ret != CAMERA\_OK) {
             OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_IsTorchSupported failed.");
        }
        if (torchModeSupported) {
             OH\_LOG\_INFO(LOG\_APP, "isTorchModeSupported success.");
        } else {
             OH\_LOG\_ERROR(LOG\_APP, "isTorchModeSupported failed. %{public}d ", ret);
        }
        return torchModeSupported;
    }
    
5.  Call [OH\_CameraManager\_SetTorchMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_settorchmode) to set the flashlight mode.
    
    Camera\_ErrorCode SetTorchMode(Camera\_Manager\* cameraManager, Camera\_TorchMode torchMode)
    {
        // Set the flashlight mode when the specified mode is supported.
        Camera\_ErrorCode ret = OH\_CameraManager\_SetTorchMode(cameraManager, torchMode);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_SetTorchMode failed. %{public}d ", ret);
        } else {
            OH\_LOG\_INFO(LOG\_APP, "OH\_CameraManager\_SetTorchMode success.");
        }
        return ret;
    }
    

#### Status Listening

During camera application development, you can listen for changes of the flashlight status, including on, off, unavailable, and available, by using the callback function.

Register the **torchStatus** event and return the listening result through a callback, which carries the **Camera\_TorchStatusInfo** parameter. For details about the parameter, see [Camera\_TorchStatusInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-torchstatusinfo).

void TorchStatusCallback(Camera\_Manager \*cameraManager, Camera\_TorchStatusInfo\* torchStatus)
{
   OH\_LOG\_INFO(LOG\_APP, "TorchStatusCallback is called.");
}
Camera\_ErrorCode RegisterTorchStatusCallback(Camera\_Manager \*cameraManager)
{
    Camera\_ErrorCode ret = OH\_CameraManager\_RegisterTorchStatusCallback(cameraManager, TorchStatusCallback);
    if (ret != CAMERA\_OK) {
       OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_RegisterTorchStatusCallback failed.");
    }
    return ret;
}
