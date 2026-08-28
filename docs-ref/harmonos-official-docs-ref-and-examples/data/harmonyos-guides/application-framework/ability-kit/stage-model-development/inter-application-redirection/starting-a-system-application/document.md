# Starting a System Application

This topic describes how to start a system application. It also lists the supported redirection capabilities of system applications.

#### Methods of Starting a System Application

In addition to the methods described in the preceding topics (for example, using **openLink** to start a specified application or using **startAbilityByType** to specify an application of the specified type), you can use the following methods to start a system application:

-   **Using Picker Components**
    
    System applications like Camera, Files, and Contacts provide **Picker** components, which allow your application to leverage their common functions without applying for permissions, for example, accessing resource files of users.
    
    An application starts a system-level **Picker** component (such as **DocumentViewPicker**, **PhotoViewPicker**, or **ContactsPicker**). The user selects files, photos, or contacts on the component, and the application obtains the result returned by the component. For example, an audio player can obtain the path of the audio file selected by the user via **AudioViewPicker**, and play the audio clip.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/Hu-SAJ-8SBWYeODZfTheVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58AB84B582A6EB18C7B9C6E9C8DA7995C16E93DD2718E585BE2270A61380683D)
    
    The system-level **Picker** components have been pre-authorized. When using such a component, you can temporarily access the corresponding resources without requesting the permissions. For example, before accessing a user's image, an application normally needs to request user authorization. However, by using **PhotoViewPicker**, the application can directly access the image selected by the user.
    
    A system-level **Picker** component is implemented by an independent system process.
    
-   **Using Specific APIs**
    
    System applications like Settings, Phone, and Calendar provide certain APIs, through which your application can directly redirect users to them.
    

#### Capabilities That Support Redirection to System Applications

## Settings

Currently, the following screens in Settings can be directly opened:

-   **Permission setting**: When an application uses [requestPermissionsFromUser()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9) to display a dialog box to request certain permissions from the user and the user rejects the request, the application cannot use this API to open the dialog box again. However, it can call [requestPermissionOnSetting](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissiononsetting12) to display a permission setting dialog box.
    
    For details about how to display the permission setting dialog box, see [Requesting User Authorization for the Second Time](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization-for-the-second-time/document.md). The sample code in this topic applies to all permissions in the [application's permission groups](../../../../../system/security/application-access-control/application-permission-management/application-permission-groups/document.md). You only need to replace the corresponding permission names. Here are some common scenarios:
    
    -   Displaying the location permission setting dialog box
    -   Displaying the camera permission setting dialog box
    -   Displaying the image and video permission setting dialog box
    -   Displaying the music and audio permission setting dialog box
    -   Displaying the contacts permission setting dialog box
    -   Displaying the calendar permission setting dialog box
-   **Notification management**: When an application uses [requestEnableNotification()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagerrequestenablenotification10) to display a dialog box for notification authorization and the user rejects the authorization, the application cannot use this API to open the dialog box again. However, it can call [openNotificationSettings()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#notificationmanageropennotificationsettings13) to display a notification management dialog box.
    
-   **Network management**: When an application needs to connect to a network through WLAN, it can call [openNetworkManagerSettings()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-settings#settingsopennetworkmanagersettings18) to display a WLAN settings dialog box.
    

| Barcode Scanning Picker | Use the camera to scan barcodes using the default UI. | [Barcode Scanning by Default UI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/scan-scanbarcode-V5) |

| Card Recognition Picker | Use the camera to recognize various certificates and extract card information. | [Card Recognition](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/vision-cardrecognition-V5) |

| Document Scanning Picker | Use the camera to shoot documents and convert them into HD scanned copies. | [Document Scanning](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/vision-documentscanner-V5) |

## Phone

[Telephony Kit](../../../../../system/network/telephony-kit/about-this-kit/document.md) provides [makeCall()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-call#callmakecall7), which allows users to jump to the dialing screen, where the number to dial is displayed.

## Calendar

[Calendar Kit](../../../../../application-services/calendar-kit/about-this-kit/document.md) provides [addEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-calendarmanager#addevent), which allows users to create a schedule.

## Contacts

[Contacts Kit](../../../../../application-services/contacts-kit/about-this-kit/document.md) provides the Contacts Picker, which is used to start the Contacts application and read contact data. For details, see [Contact Selection](../../../../../application-services/contacts-kit/about-this-kit/document.md#contact-selection-with-picker).

| AppGallery | Show App Details | [loadProduct](https://developer.huawei.com/consumer/en/doc/harmonyos-references-V5/store-productviewmanager-V5#section144826162913) |

## Files

[Core File Kit](../../../../core-file-kit/about-this-kit/document.md) provides the DocumentViewPicker and AudioViewPicker.

-   The DocumentViewPicker is used to access and save documents in the public directory. For details, see [Selecting Documents](../../../../core-file-kit/user-files/selecting-and-saving-user-files/selecting-user-files/document.md#selecting-documents) and [Saving Documents](../../../../core-file-kit/user-files/selecting-and-saving-user-files/saving-user-files/document.md#saving-documents).
-   The AudioViewPicker is used to access and save audio files in the public directory. For details, see [Selecting Audio Clips](../../../../core-file-kit/user-files/selecting-and-saving-user-files/selecting-user-files/document.md#selecting-audio-clips) and [Saving Audio Clips](../../../../core-file-kit/user-files/selecting-and-saving-user-files/saving-user-files/document.md#saving-audio-clips).

## Gallery (Media Library)

[Media Library Kit](../../../../../media/media-library-kit/about-this-kit/document.md) provides the PhotoViewPicker for accessing and saving images or video files in the public directory. For details, see [Selecting Media Assets Using Picker](../../../../../media/media-library-kit/selecting-media-assets-using-picker/document.md) and [Creating a Media Asset Using SaveButton](../../../../../media/media-library-kit/saving-media-assets/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/OO8i3lsFSQq9B-WLAI4q0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B2FAA62994482500147EC953224D04DD42F91B5B0A09A6ACC359FAF1721E290)

APIs related to startup settings are under planning.
