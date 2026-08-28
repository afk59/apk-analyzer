# Device Input Management (C/C++)

Before developing a camera application, you must [request required permissions](../../requesting-camera-development-permissions/document.md).

A camera application invokes and controls a camera device to perform basic operations such as preview, photo capture, and video recording.

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
    
3.  Call [OH\_CameraManager\_CreateCameraInput()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcamerainput) to obtain a cameraInput object.
    
    // Listen for camera input errors.
    void OnCameraInputError(const Camera\_Input\* cameraInput, Camera\_ErrorCode errorCode)
    {
       OH\_LOG\_INFO(LOG\_APP, "OnCameraInput errorCode: %{public}d", errorCode);
    }
    
    CameraInput\_Callbacks\* GetCameraInputListener(void)
    {
       static CameraInput\_Callbacks cameraInputCallbacks = {
          .onError = OnCameraInputError
       };
       return &cameraInputCallbacks;
    }
    
    // Listen for camera status information.
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
    
    void CreateAndOpenCamera()
    {
        Camera\_Manager\* cameraManager = nullptr;
        Camera\_Input\* cameraInput = nullptr;
        Camera\_Device\* cameras = nullptr;
        uint32\_t size = 0;
        uint32\_t cameraDeviceIndex = 0;
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
         if (cameras == nullptr || size == 0 || ret != CAMERA\_OK) {
             OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedCameras failed.");
             return;
         }
        // Create a camera input stream.
        ret = OH\_CameraManager\_CreateCameraInput(cameraManager, &cameras\[cameraDeviceIndex\], &cameraInput);
        if (cameraInput == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_CreateCameraInput failed.");
            return;
        }
        ret = OH\_CameraInput\_RegisterCallback(cameraInput, GetCameraInputListener());
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraInput\_RegisterCallback failed.");
        }
        // Open a camera.
        ret = OH\_CameraInput\_Open(cameraInput);
        if (ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraInput\_open failed.");
            return;
        }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/Iypw27HJT-i0gWsL7yI1dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C5972633D4349595CC1EB0D4D6832CAC8FE3EDFABA1807BDBAF99A8CBA4365C)
    
    Before any camera device input, you must complete camera management by following the instructions provided in [Camera Device Management](../camera-device-management-c-c/document.md).
    
4.  Call [OH\_CameraManager\_GetSupportedSceneModes()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedscenemodes) to obtain the list of scene modes supported by the current camera device. The list stores all the [Camera\_SceneMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_scenemode) supported by the camera device.
    
    bool IsSupportedSceneMode(Camera\_Device camera, Camera\_SceneMode sceneMode)
    {
        Camera\_SceneMode\* sceneModes = nullptr;
        uint32\_t sceneModeSize = 0;
        Camera\_ErrorCode ret = OH\_CameraManager\_GetSupportedSceneModes(&camera, &sceneModes, &sceneModeSize);
        if (sceneModes == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedSceneModes failed.");
            return false;
        }
        for (uint32\_t index = 0; index < sceneModeSize; index++) {
            OH\_LOG\_INFO(LOG\_APP, "scene mode = %{public}u ", sceneModes\[index\]);    // Obtain the specified scene mode.
            if (sceneModes\[index\] == sceneMode) {
                return true;
            }
        }
        return false;
    }
    
5.  Call [OH\_CameraManager\_GetSupportedCameraOutputCapabilityWithSceneMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameraoutputcapabilitywithscenemode) to obtain all output streams supported by the camera device in the current mode, such as preview and photo streams. Output streams are specified in the **profile** fields of [Camera\_OutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-camera-camera-outputcapability). Add the output stream of the corresponding type to the session based on the [camera scene mode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_scenemode). For details, see step 6 in [How to Develop](../camera-session-management-c-c/document.md#how-to-develop) of camera session management.
    
    Camera\_OutputCapability\* GetSupportedCameraOutputCapability(Camera\_Manager\* cameraManager, Camera\_Device &camera)
    {
        Camera\_OutputCapability\* cameraOutputCapability = nullptr;
        // The following sample code checks whether the NORMAL\_PHOTO mode is supported by the camera.
        bool isSupported = IsSupportedSceneMode(camera, Camera\_SceneMode::NORMAL\_PHOTO);
        if (!isSupported) {
            OH\_LOG\_ERROR(LOG\_APP, "NORMAL\_PHOTO is not supported.");
            return cameraOutputCapability;
        }
        // Obtain the output stream capability supported by the camera.
        const Camera\_Profile\* previewProfile = nullptr;
        const Camera\_Profile\* photoProfile = nullptr;
        Camera\_ErrorCode ret = OH\_CameraManager\_GetSupportedCameraOutputCapabilityWithSceneMode(cameraManager, &camera,
            Camera\_SceneMode::NORMAL\_PHOTO, &cameraOutputCapability);
        if (cameraOutputCapability == nullptr || ret != CAMERA\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_CameraManager\_GetSupportedCameraOutputCapability failed.");
            return cameraOutputCapability;
        }
        // The following uses the NORMAL\_PHOTO mode as an example. You need to add the preview stream and photo stream.
        if (cameraOutputCapability->previewProfiles == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "previewProfiles == null");
        } else {
            // Select an appropriate preview resolution from previewProfiles of cameraOutputCapability.
            previewProfile = cameraOutputCapability->previewProfiles\[0\];
        }
        if (cameraOutputCapability->photoProfiles == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "photoProfiles == null");
        } else {
            // Select an appropriate photo resolution from photoProfiles of cameraOutputCapability.
            photoProfile = cameraOutputCapability->photoProfiles\[0\];
        }
        return cameraOutputCapability;
    }
