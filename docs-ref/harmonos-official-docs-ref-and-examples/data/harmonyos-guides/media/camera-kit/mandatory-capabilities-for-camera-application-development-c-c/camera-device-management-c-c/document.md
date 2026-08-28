# Camera Device Management (C/C++)

Before developing a camera application, you must call the camera APIs to create an independent camera device.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera) for the API reference.

1.  Import the NDK.
    
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
    
    target\_link\_libraries(entry PUBLIC
        libace\_napi.z.so
        libohcamera.so
        libhilog\_ndk.z.so
    )
    
3.  Call [OH\_Camera\_GetCameraManager()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#oh_camera_getcameramanager) to obtain a cameraManager object.
    
    Camera\_ErrorCode CreateCameraManager(Camera\_Manager\*\* cameraManager)
    {
        // Create a CameraManager object.
        Camera\_ErrorCode ret = OH\_Camera\_GetCameraManager(cameraManager);
        if (\*cameraManager == nullptr || ret != CAMERA\_OK) {
           OH\_LOG\_ERROR(LOG\_APP, "OH\_Camera\_GetCameraManager failed.");
        }
        return ret;
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/V4z_hZPaQHqY3ANadxR4uw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14730430CC6B37A131FF4C612584643D2FB9509A238FD67DE719F743F008E121)
    
    If obtaining the object fails, the camera device may be occupied or unusable. If it is occupied, wait until it is released.
    
4.  Call [OH\_CameraManager\_GetSupportedCameras()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameras) to obtain the list of cameras supported by the current device. The list stores the IDs of all cameras supported. If the list is not empty, each ID in the list can be used to create an independent camera object. If the list is empty, no camera is available for the current device and subsequent operations cannot be performed.
    
    Camera\_ErrorCode GetSupportedCameras(Camera\_Manager\* cameraManager, Camera\_Device\*\* cameras, uint32\_t &size)
    {
        // Obtain the camera list.
        Camera\_ErrorCode ret = OH\_CameraManager\_GetSupportedCameras(cameraManager, cameras, &size);
        if (cameras == nullptr || size == 0 || ret != CAMERA\_OK) {
           OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedCameras failed.");
        }
        // If cameras are no longer needed, call delete\[\] to release the memory.
        for (uint32\_t index = 0; index < size; index++) {
           OH\_LOG\_INFO(LOG\_APP, "cameraId  =  %{public}s ", (\*cameras)\[index\].cameraId);              // Obtain the camera ID.
           OH\_LOG\_INFO(LOG\_APP, "cameraPosition  =  %{public}d ", (\*cameras)\[index\].cameraPosition);  // Obtain the camera position.
           OH\_LOG\_INFO(LOG\_APP, "cameraType  =  %{public}d ", (\*cameras)\[index\].cameraType);          // Obtain the camera type.
           OH\_LOG\_INFO(LOG\_APP, "connectionType  =  %{public}d ", (\*cameras)\[index\].connectionType);  // Obtain the camera connection type.
        }
        return ret;
    }
    

#### Status Listening

During camera application development, you can listen for the camera status, including the appearance of a new camera, removal of a camera, and availability of a camera. The camera ID and camera status are included in the callback function. When a new camera appears, the new camera can be added to the supported camera list.

Call [OH\_CameraManager\_RegisterCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_registercallback) to register the **'cameraStatus'** event and return the listening result through a callback, which carries the **Camera\_StatusInfo** parameter. For details about the parameter, see [Camera\_StatusInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-statusinfo).

void CameraStatusCallback(Camera\_Manager\* cameraManager, Camera\_StatusInfo\* status)
{
   OH\_LOG\_INFO(LOG\_APP, "CameraStatusCallback is called");
}
CameraManager\_Callbacks\* GetCameraManagerListener()
{
   static CameraManager\_Callbacks cameraManagerListener = {
      .onCameraStatus = CameraStatusCallback
   };
   return &cameraManagerListener;
}

Camera\_ErrorCode RegisterCameraStatusCallback(Camera\_Manager &cameraManager)
{
    Camera\_ErrorCode ret = OH\_CameraManager\_RegisterCallback(&cameraManager, GetCameraManagerListener());
    if (ret != CAMERA\_OK) {
       OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_RegisterCallback failed.");
    }
    return ret;
}
