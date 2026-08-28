# Open user\_grant Permissions

All the permissions in this topic are available to all applications and granted by the user.

This type of permissions must be declared in the application installation package and authorized by the user in a dialog box during the running of the application. The application has the permission only after the user has granted the permission.

#### Request Mode

The [user\_grant permissions](../../application-permission-management-overview/document.md#user_grant-user-authorization) are permissions granted by users. For details about how to request this type of permissions, see [Declaring Permissions](../../requesting-application-permissions/declaring-permissions/document.md) > [Requesting User Authorization](../../requesting-application-permissions/requesting-user-authorization/document.md).

#### ohos.permission.ACCESS\_BLUETOOTH

Allows an application to access Bluetooth.

This permission enables features such as scanning, discovering, pairing with, and connecting to nearby Bluetooth devices, as well as advertising and scanning for Bluetooth Low Energy devices.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 10

#### ohos.permission.MEDIA\_LOCATION

Allows an application to access geographical locations in the user's media file.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 7

#### ohos.permission.APP\_TRACKING\_CONSENT

Allows an application to read the open anonymous device identifier (OAID).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/IEqYMuEeSTG7zcwsPz0zuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2698C6B6058B8E8D46D29FD22B042ED175BEC8A79818AFD9D1424EBA667AE55)

When applying for this permission, whether a dialog box is displayed to request authorization from the user depends on whether the application is required to request association.

-   If not, the system does not display a dialog box when an application requests a permission. The application permission is granted by default.
-   If yes, the system will display a dialog box when an application requests permissions. The application can be granted permissions only after the user confirms the request.

You can check whether the application is required to request association on the Settings > Privacy & security > Cross-app association screen.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 9

#### ohos.permission.ACTIVITY\_MOTION

Allows an application to read the current workout status of the user, such as detecting whether the user is working out and recording the number of steps the user has taken.

For example, to determine whether the user is in motion or to record the number of steps that the user has walked.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 7

#### ohos.permission.CAMERA

Allows an application to use the camera.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 9

#### ohos.permission.DISTRIBUTED\_DATASYNC

Allows the application data to be exchanged between devices.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 7

#### ohos.permission.LOCATION\_IN\_BACKGROUND

Allows an application running in the background to obtain the device location.

**Procedure**:

1.  [Declare permissions](../../requesting-application-permissions/declaring-permissions/document.md) in the **module.json5** file.
    
    You must request the foreground location permission before requesting the background location permission. Therefore, you must declare both of them. The foreground location permissions include the following:
    
    -   Apply for the foreground approximate location permission: Declare [ohos.permission.APPROXIMATELY\_LOCATION](#ohospermissionapproximately_location).
    -   Apply for the foreground precise location permission: Declare both the [ohos.permission.APPROXIMATELY\_LOCATION](#ohospermissionapproximately_location) and [ohos.permission.LOCATION](#ohospermissionlocation) permissions.
2.  The application calls [requestPermissionsFromUser()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9) to display a dialog box to request the foreground location permission from the user.
    
3.  If the user clicks to allow the application to use the foreground location permission in the pop-up window, the application can guide the user to grant the background location permission in the system settings. If the user denies the application's use of the foreground location permission, the application can guide the user to grant the permission in the system settings, or call [requestPermissionOnSetting()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissiononsetting12) to open the permission settings pop-up window again to guide the user to grant the permission.
    

The system provides the continuous task mechanism. For applications that need to use the location in the background, you can request the continuous task of the **LOCATION** type and the foreground location permission to obtain the location in the background without requesting the background location permission. For details, see [Continuous Task](../../../../../../application-framework/background-tasks-kit/continuous-task-arkts/document.md).

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 7

#### ohos.permission.LOCATION

Allows an application to obtain the device location.

**Prerequisites**: This permission must be requested with [ohos.permission.APPROXIMATELY\_LOCATION](#ohospermissionapproximately_location) together.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 7

#### ohos.permission.APPROXIMATELY\_LOCATION

Allows an application to obtain the approximate location information of a device.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 9

#### ohos.permission.MICROPHONE

Allows an application to access the microphone.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 8

#### ohos.permission.READ\_CALENDAR

Allows an application to read Calendar data.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 8

#### ohos.permission.WRITE\_CALENDAR

Allows an application to add, remove, and modify Calendar events.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 8

#### ohos.permission.READ\_HEALTH\_DATA

Allows an application to read the health data of the user.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 7

#### ohos.permission.ACCESS\_NEARLINK

Allows an application to use NearLink, such as device pairing and connecting to nearby devices.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 12

#### ohos.permission.READ\_WRITE\_DOWNLOAD\_DIRECTORY

Allows an application to access the **Download** directory and its subdirectories in the user directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/ftnX-aVSRQKVFy0Lp7zF2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F74F856086507AD7BFC1BD6DB77BF5919CC4CD85A4D6731AFFA19C10D1AD2A7)

The permission level has changed. To ensure compatibility, request this permission by following the procedure in [Requesting Restricted Permissions](../../requesting-application-permissions/requesting-restricted-permissions/document.md) in the current version.

**Permission level**: normal

**Authorization mode**: user\_grant

**Supported devices**: PCs/2-in-1 devices | tablets

**Valid since**: 11

**Changelog**: The permission level is system\_basic in API version 11, and is changed to normal since API version 12.

#### ohos.permission.READ\_WRITE\_DOCUMENTS\_DIRECTORY

Allows an application to access the **Documents** directory and its subdirectories in the user directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/yeH_u196RcquooheaOjALA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAD21B06924860461732F0DA1529C8861DCF7609848145F0D9876B96D043E925)

The permission level has changed. To ensure compatibility, request this permission by following the procedure in [Requesting Restricted Permissions](../../requesting-application-permissions/requesting-restricted-permissions/document.md) in the current version.

**Permission level**: normal

**Authorization mode**: user\_grant

**Supported devices**: PCs/2-in-1 devices | tablets

**Valid since**: 11

**Changelog**: The permission level is system\_basic in API version 11, and is changed to normal since API version 12.

#### ohos.permission.CUSTOM\_SCREEN\_CAPTURE

Allows an application to capture screen information.

With this permission, the application can perform operations such as taking screenshots.

**Permission level**: normal

**Authorization mode**: user\_grant

**Supported devices**: PCs/2-in-1 devices | tablets | phones

**Valid since**: 14

**Changelog**: This permission is available only on tablets and PCs/2-in-1 devices from API versions 14 to 20. Since API version 21, this permission is also available on phones.

#### ohos.permission.READ\_MEDIA

Allows an application to read media files from the user's external storage.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 7

**Deprecated from**: 22

**Substitute**:

See the [alternative solution of the **Files** permission group](../../application-permission-groups/document.md#filesdeprecated).

#### ohos.permission.WRITE\_MEDIA

Allows an application to read media files from and write media files into the user's external storage.

**Permission level**: normal

**Authorization mode**: user\_grant

**Valid since**: 7

**Deprecated from**: 22

**Substitute**:

See the [alternative solution of the **Files** permission group](../../application-permission-groups/document.md#filesdeprecated).
