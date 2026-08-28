# Application Permission Groups

#### Usage Guidelines

-   It will be helpful if you understand [permission groups and permissions](../application-permission-management-overview/document.md#permission-groups-and-permissions) before requesting permission groups for your application.
    
-   It helps minimize the number of dialogs that are presented to the user when an application requests closely related permissions. The user simply needs to grant the permissions all at once, except for the Location, Contacts, and Calendar permission groups.
    
    The following uses the Location and Camera permission groups as an example.
    
    -   When an application requests only the ohos.permission.APPROXIMATELY\_LOCATION permission (belong to the Location permission group), a dialog box containing only the requested permission will be displayed to request user authorization.
    -   When an application requests the ohos.permission.APPROXIMATELY\_LOCATION and ohos.permission.LOCATION permissions (belonging to the Location permission group), a dialog box containing only the requested permissions will be displayed to request user authorization.
    -   When an application requests ohos.permission.APPROXIMATELY\_LOCATION (belonging to the Location permission group) and ohos.permission.CAMERA (belonging to the Camera permission group), two dialog boxes will be displayed to request the location and camera permissions, respectively.
-   The following lists the permission groups supported by the system. For details about the meaning of each permission, see [the permission list](../application-permissions/open-user-grant-permissions/document.md).
    

#### Location

-   [ohos.permission.LOCATION\_IN\_BACKGROUND](../application-permissions/open-user-grant-permissions/document.md#ohospermissionlocation_in_background)
    
-   [ohos.permission.LOCATION](../application-permissions/open-user-grant-permissions/document.md#ohospermissionlocation)
    
-   [ohos.permission.APPROXIMATELY\_LOCATION](../application-permissions/open-user-grant-permissions/document.md#ohospermissionapproximately_location)
    

#### Camera

-   [ohos.permission.CAMERA](../application-permissions/open-user-grant-permissions/document.md#ohospermissioncamera)

#### Microphone

-   [ohos.permission.MICROPHONE](../application-permissions/open-user-grant-permissions/document.md#ohospermissionmicrophone)

#### Contacts

-   [ohos.permission.READ\_CONTACTS](../application-permissions/restricted-permissions/document.md#ohospermissionread_contacts)
    
-   [ohos.permission.WRITE\_CONTACTS](../application-permissions/restricted-permissions/document.md#ohospermissionwrite_contacts)
    

#### Calendar

-   [ohos.permission.READ\_CALENDAR](../application-permissions/open-user-grant-permissions/document.md#ohospermissionread_calendar)
    
-   [ohos.permission.WRITE\_CALENDAR](../application-permissions/open-user-grant-permissions/document.md#ohospermissionwrite_calendar)
    
-   [ohos.permission.READ\_WHOLE\_CALENDAR](../application-permissions/restricted-permissions/document.md#ohospermissionread_whole_calendar)
    
-   [ohos.permission.WRITE\_WHOLE\_CALENDAR](../application-permissions/restricted-permissions/document.md#ohospermissionwrite_whole_calendar)
    

#### Fitness

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/E9ZFIxWMSvem_WLVori58w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBA2AE769CA89B4F0D2F3920FAE15757923F140D71F675FA3163AA31BC9A3EE2)

This permission is not available to 2-in-1 device applications because such devices do not have related sensors.

-   [ohos.permission.ACTIVITY\_MOTION](../application-permissions/open-user-grant-permissions/document.md#ohospermissionactivity_motion)

#### Body Sensors

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/tSNAeKhATj-igP2G19DNYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6248F420BB4017F9CC9A09BB2D61945D02423AB6CFDE2FAE7E18BAFBBC8C0A8)

This permission is available only to wearable device applications.

-   [ohos.permission.READ\_HEALTH\_DATA](../application-permissions/open-user-grant-permissions/document.md#ohospermissionread_health_data)

#### Images and Videos

-   [ohos.permission.WRITE\_IMAGEVIDEO](../application-permissions/restricted-permissions/document.md#ohospermissionwrite_imagevideo)
    
-   [ohos.permission.READ\_IMAGEVIDEO](../application-permissions/restricted-permissions/document.md#ohospermissionread_imagevideo)
    
-   [ohos.permission.MEDIA\_LOCATION](../application-permissions/open-user-grant-permissions/document.md#ohospermissionmedia_location)
    

#### Music and Audio

-   [ohos.permission.WRITE\_AUDIO](../application-permissions/restricted-permissions/document.md#ohospermissionwrite_audio)
    
-   [ohos.permission.READ\_AUDIO](../application-permissions/restricted-permissions/document.md#ohospermissionread_audio)
    

#### Cross-Application Association

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/l9kJVWU2RjyLLzXbA_p3Dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F36D74C2665AAB6CBE77C8AEEEF4450A17DDD4D645EF4FF8F60F3D6619D63C6)

When applying for this permission, whether a dialog box is displayed to request authorization from the user depends on whether the application is required to request association.

-   If not, the system does not display a dialog box when an application requests a permission. The application permission is granted by default.
-   If yes, the system will display a dialog box when an application requests permissions. The application can be granted permissions only after the user confirms the request.

You can check whether the application is required to request association on the Settings > Privacy & security > Cross-app association screen.

-   [ohos.permission.APP\_TRACKING\_CONSENT](../application-permissions/open-user-grant-permissions/document.md#ohospermissionapp_tracking_consent)

#### Device Discovery and Connection

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/OHjK0Op6RcOZkgNW76bS3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F65E108762C5E718647D2E9D1076B9827D5BE0C070A83FE25995BF6CB4D38F9)

Since API 13, the original Bluetooth, NearLink, and multi-device collaboration permission groups are no longer used. Related permissions will be granted and operated through the device discovery and connection permission group.

-   [ohos.permission.ACCESS\_BLUETOOTH](../application-permissions/open-user-grant-permissions/document.md#ohospermissionaccess_bluetooth)
-   [ohos.permission.ACCESS\_NEARLINK](../application-permissions/open-user-grant-permissions/document.md#ohospermissionaccess_nearlink)
-   [ohos.permission.DISTRIBUTED\_DATASYNC](../application-permissions/open-user-grant-permissions/document.md#ohospermissiondistributed_datasync)

#### Pasteboard

-   [ohos.permission.READ\_PASTEBOARD](../application-permissions/restricted-permissions/document.md#ohospermissionread_pasteboard)

#### Screenshots

-   [ohos.permission.CUSTOM\_SCREEN\_CAPTURE](../application-permissions/open-user-grant-permissions/document.md#ohospermissioncustom_screen_capture)

#### Directory

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/dcR-cYm7SweIczHGSzKkgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94C791D58624AF991359B2502553A3001D1EDA15311C3ADEDC56C1498E466D96)

The permissions are available only to 2-in-1 device applications.

-   [ohos.permission.READ\_WRITE\_DOWNLOAD\_DIRECTORY](../application-permissions/open-user-grant-permissions/document.md#ohospermissionread_write_download_directory)
    
-   [ohos.permission.READ\_WRITE\_DESKTOP\_DIRECTORY](../application-permissions/restricted-permissions/document.md#ohospermissionread_write_desktop_directory)
    
-   [ohos.permission.READ\_WRITE\_DOCUMENTS\_DIRECTORY](../application-permissions/open-user-grant-permissions/document.md#ohospermissionread_write_documents_directory)
    

#### Files(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/UOpevkC8RwyhXdRLnpp9JA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3C1F4C0301E86738D9EA21CE770F268DD82C0B8DAF75C5652CE307816D41F20)

Since API version 9, alternatives are supported.

-   ohos.permission.READ\_MEDIA
    
-   ohos.permission.WRITE\_MEDIA
    

**Alternative solution**:

-   To read or write images/videos in the media library:
    
    -   Recommended solution (no permission required): Use [Picker](../../../../../media/media-library-kit/selecting-media-assets-using-picker/document.md) to read images and videos from the media library. Use the [Save button/Authorization dialog box](../../../../../media/media-library-kit/saving-media-assets/document.md) to save images and videos from the media library.
    -   Request the restricted permission [ohos.permission.READ\_IMAGEVIDEO](../application-permissions/restricted-permissions/document.md#ohospermissionread_imagevideo) or [ohos.permission.WRITE\_IMAGEVIDEO](../application-permissions/restricted-permissions/document.md#ohospermissionwrite_imagevideo).
-   To read and write audio clips in the media library:
    
    Request the restricted permission [ohos.permission.READ\_AUDIO](../application-permissions/restricted-permissions/document.md#ohospermissionread_audio) or [ohos.permission.WRITE\_AUDIO](../application-permissions/restricted-permissions/document.md#ohospermissionwrite_audio).
    
-   Read files in the file manager.
    
    Use the file Picker to read documents in **Files**. For details, see [Selecting Documents](../../../../../application-framework/core-file-kit/user-files/selecting-and-saving-user-files/selecting-user-files/document.md#selecting-documents) and [Saving Documents](../../../../../application-framework/core-file-kit/user-files/selecting-and-saving-user-files/saving-user-files/document.md#saving-documents).
