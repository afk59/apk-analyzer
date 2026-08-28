# Requesting Camera Development Permissions

The main process of camera application development includes development preparations, device input management, session management, preview, photo capture, and video recording.

Before developing a camera application, you must request camera-related permissions to ensure that the application has the permission to access the camera device and other services. Before requesting permissions, ensure that the [basic principles for using permissions](../../../system/security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions) are met.

-   To use the camera for photo capture, request the ohos.permission.CAMERA permission.
-   To use the microphone to record audio, request the ohos.permission.MICROPHONE permission.
-   To display location information in photos or videos captured, request the ohos.permission.MEDIA\_LOCATION permission.

All these permissions must be authorized by users through a dialog box. For details about how to request and verify the permissions, see [Declaring Permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md) and [Requesting User Authorization](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

-   To read images or videos, you are advised to use the media library [Picker to access them](../../media-library-kit/selecting-media-assets-using-picker/document.md).
-   To save images or videos, use the [security components to save them](../../media-library-kit/saving-media-assets/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/LK4BUwlZS4Svo37uRHTg1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DA3B4D25D240D8161B45226E15DC7CA3002DCC5DA27683187DFC7147B4E3073)

When the application needs to clone, back up, or synchronize images and videos in users' public directory, request the ohos.permission.READ\_IMAGEVIDEO and ohos.permission.WRITE\_IMAGEVIDEO permissions for reading and writing audio files. For details, see [Requesting Restricted Permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md), which can be used only after being approved by AppGallery Connect (AGC). To prevent the application release request from being rejected, you are advised to use alternative solutions such as Pickers and components preferentially. Restricted permissions are granted only when the [related conditions are met](../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md#ohospermissionread_imagevideo).
