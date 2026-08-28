# AR Engine Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/XcnkJp_1QDOOsBoNUubooQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A72D8E1726045AD59CDCFDA4366444F627609DD87B0B73A803BB0487A6532A8)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../api-reference-overview/universal-error-codes/document.md).

If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/). Huawei technical support will handle it in time.

#### 1009200001 API Call Failure

**Message**

Failure.

**Description**

The API fails to be called.

**Possible causes**

This error code indicates a common running error, such as the failure to build an object.

**Solution**

Restart the app. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/). Huawei technical support will handle it in time.

#### 1009200002 Session Paused

**Message**

Session paused.

**Description**

The session is paused.

**Possible causes**

The current session is paused or is not resumed.

**Solution**

Call [HMS\_AREngine\_ARSession\_Resume](../c-apis/modules/ar-engine/document.md#ga7138d56b767738b8aadcbc74f4c328db) to restart the session.

#### 1009200003 Session Not Paused

**Message**

Session not paused.

**Description**

The session is not paused.

**Possible causes**

The current session is in running status.

**Solution**

Call [HMS\_AREngine\_ARSession\_Pause](../c-apis/modules/ar-engine/document.md#ga09dedb5c633141321591db0981629de1) to pause the current session.

#### 1009200004 Not Tracking

**Message**

Not tracking.

**Description**

The session is not in the tracking state during the process of obtaining the target anchor or plane information

**Possible causes**

The current session is abnormal.

**Solution**

Check whether the current session object (which is of the [AREngine\_ARSession](../c-apis/modules/ar-engine/document.md#ga2dbf3585f50628750ec855501c043650) type) is empty.

#### 1009200005 Texture Not Set

**Message**

Texture not set.

**Description**

No GL texture is set.

**Possible causes**

The GL texture used for rendering is not set.

**Solution**

Check whether [HMS\_AREngine\_ARSession\_SetCameraGLTexture()](../c-apis/modules/ar-engine/document.md#gac697e4be36db63ed6098f154aa9ac01c) is used to set the correct GL texture.

#### 1009200006 GL Context Missing

**Message**

GL context missing.

**Description**

No OpenGL context exists.

**Possible causes**

The current thread lacks the OpenGL context. Calling [eglGetCurrentContext()](https://registry.khronos.org/EGL/sdk/docs/man/html/eglGetCurrentContext.xhtml) returns **EGL\_NO\_CONTEXT**.

**Solution**

Check whether [HMS\_AREngine\_ARSession\_Update()](../c-apis/modules/ar-engine/document.md#ga1d1cacf372a8011a439f0e4e76994259) is called in the OpenGL rendering thread.

#### 1009200007 Configuration Not Supported

**Message**

Configuration not supported.

**Description**

AR Engine does not support the current configuration.

**Possible causes**

Preview dimensions are not supported.

**Solution**

Call [OH\_CameraManager\_GetSupportedCameraOutputCapability](../../../media/camera-kit/c-apis/header-files/camera-manager-h/document.md#oh_cameramanager_getsupportedcameraoutputcapability) to check whether the preview dimensions are supported.

#### 1009200008 Resource Exhausted

**Message**

Resource exhausted.

**Description**

The memory is used up.

**Possible causes**

The memory is insufficient, and the memory allocation fails.

**Solution**

Check whether the memory is sufficient. If not, prompt the user to clear the memory. If the memory is sufficient, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/). Huawei technical support will handle it in time.

#### 1009200009 Service Unavailable

**Message**

Service unavailable.

**Description**

The service is unavailable.

**Possible causes**

The device does not support this service.

**Solution**

Check whether the device is in the [Hardware Requirements](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-preparations#section143821139152310). If so, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/). Huawei technical support will handle it in time.

#### 1009200010 Camera Unavailable

**Message**

Camera unavailable.

**Description**

The camera is unavailable.

**Possible causes**

AR Engine cannot open the camera as it is occupied by other processes.

**Solution**

Check whether the camera is occupied by other processes when your app calls AR Engine. If not, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/). Huawei technical support will handle it in time.

#### 1009200011 The Number of Images to Be Added Exceeds the Upper Limit

**Message**

The number of images added exceeds the maximum.

**Description**

The number of images added exceeds the maximum.

**Possible causes**

The number of images to be added exceeds the upper limit.

**Solution**

Check whether the number of images added to the tracking image database exceeds the upper limit.

1.  If ArkTS is used for development, you can obtain the maximum number of images using [ARAugmentedImageDatabase.getCapacity](../arkts-apis/arengine-ar-capabilities/document.md#section87071617088) and the number of images stored in the database using [ARAugmentedImageDatabase.getImageCount](../arkts-apis/arengine-ar-capabilities/document.md#section106577102812).
2.  If C/C++ is used for development, you can obtain the maximum number of images using [HMS\_AREngine\_ARAugmentedImageDatabase\_GetCapacity](../c-apis/modules/ar-engine/document.md#section650873916491) and the number of images stored in the database using [HMS\_AREngine\_ARAugmentedImageDatabase\_GetImageCount](../c-apis/modules/ar-engine/document.md#section6183812506).

If the preceding requirements are met, you can [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/). Huawei technical support will handle it in time.

#### 1009200012 Attempting to Add a Low-Quality Image to the Image Database

**Message**

Attempted to add an image with insufficient quality to the image database.

**Description**

An attempt was made to add a low-quality image to the image database.

**Possible causes**

An attempt was made to add a low-quality image to the image database.

**Solution**

Check whether the app attempted to add a low-quality image to the image database. For details, please refer to [ARAddAugmentedImageReason](../arkts-apis/arengine-ar-capabilities/document.md#section7453144131020). If the image meets the requirements, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/). Huawei technical support will handle it in time.

#### 1009200013 No Valid Image Database

**Message**

No valid image database.

**Description**

No valid image database exists.

**Possible causes**

The image database is not created.

**Solution**

Check whether an image database is created using [HMS\_AREngine\_ARAugmentedImageDatabase\_Create](../c-apis/modules/ar-engine/document.md#section4108822184411).

If so, you can [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/). Huawei technical support will handle it in time.

#### 1009200014 The Pictures Cannot Be Added When the Tracking State Is Running

**Message**

The pictures cannot be added when the tracking state is running.

**Description**

The pictures cannot be added when the tracking state is running.

**Possible causes**

The program is in the tracking state.

**Solution**

Ensure that [AREngine\_ARTrackingState](../c-apis/modules/ar-engine/document.md#gaae57d2f58331e1033b60cdb2d506a382) is set to **ARENGINE\_TRACKING\_STATE\_PAUSED** or **ARENGINE\_TRACKING\_STATE\_STOPPED**.

#### 1009200015 NativeBuffer Creation Failed

**Message**

Failed to create nativeBuffer.

**Description**

Failed to create NativeBuffer.

**Possible causes**

The heap memory is exhausted.

**Solution**

Check the device's memory status and ensure that adequate heap memory is available. If the error persists, restart the device.

#### 1009200016 Failed to Write to NativeBuffer

**Message**

Failed to write nativeBuffer.

**Description**

Failed to write to NativeBuffer.

**Possible causes**

The heap memory is exhausted.

**Solution**

Check the device's memory status and ensure that adequate heap memory is available. If the error persists, restart the device.

#### 1009200017 Camera Service Error

**Message**

The camera service is abnormal.

**Description**

The camera service is abnormal.

**Possible causes**

The camera service is abnormal, for example, the service restarts or an IPC exception occurs.

**Solution**

Create the service again.

#### 1009200201 Invalid Operation Status

**Message**

ARView invalid operation.

**Description**

The ARView operation is not standard.

**Possible causes**

The config/callBack and other related settings are repeatedly performed after ARViewContext is initialized.

**Solution**

Check whether the sample code is used according to the [ARViewContext](../arkts-apis/arviewcontroller-ar-scene-management-capabilities/document.md#section12681656121519) sample code.

#### 1009200202 Graphics3D AR Scene Required

**Message**

Graphics3D AR scene required.

**Description**

The AR scene is missing.

**Possible causes**

The AR scene - [ARViewContext.scene](../arkts-apis/arviewcontroller-ar-scene-management-capabilities/document.md#section885612613616) is not set before ARViewContext is initialized.

**Solution**

Set the AR scene before initializing [ARViewContext](../arkts-apis/arviewcontroller-ar-scene-management-capabilities/document.md#section12681656121519). For details, please refer to [Managing AR Sessions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-arsession).

#### 1009200203 ARViewContext.Config Required

**Message**

AREngine config required.

**Description**

ARViewContext.config is not configured.

**Possible causes**

**ARViewContext.config** is not configured before **ARViewContext** is initialized.

**Solution**

Configure **ARViewContext.config** before initializing [ARViewContext](../arkts-apis/arviewcontroller-ar-scene-management-capabilities/document.md#section12681656121519). For details, please refer to [Managing AR Sessions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arengine-arsession).

#### 1009200204 AR Session Setup Failed

**Message**

AR session setup failed.

**Description**

The AR session fails to be initialized.

**Possible causes**

The AR session fails to be initialized because config is not correctly set.

**Solution**

Check the error code returned when the related API is called and reset the error code as prompted.

#### 1009200205 AR Scene Camera Setup Failed

**Message**

AR scene camera setup failed.

**Description**

The AR scene camera node fails to be created.

**Possible causes**

The camera node fails to be created due to resource exhaustion or repeated camera creation.

**Solution**

Check whether the [ARViewContext](../arkts-apis/arviewcontroller-ar-scene-management-capabilities/document.md#section12681656121519) API is called to initialize ARView, and whether the camera is confirmed or the system has sufficient memory. If not, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/). Huawei technical support will handle it in time.
