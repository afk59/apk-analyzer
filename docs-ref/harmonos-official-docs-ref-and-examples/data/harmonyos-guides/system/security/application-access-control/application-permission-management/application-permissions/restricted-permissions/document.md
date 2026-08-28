# Restricted Permissions

#### How to Request

Currently, only few applications for special scenarios can use restricted permissions after being approved. For details about how to request restricted permissions, see [Requesting Restricted Permissions](../../requesting-application-permissions/requesting-restricted-permissions/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/afBKA_k5QTuVH95a-PoW_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD6BADACA2847E6720BDDACB6457BA5F59A8D3CE5C08F845018307AE584C6056)

Applications that require restricted permissions will undergo a review during submission for release in AppGallery Connect (AGC). If the application does not pass the review, its release request will be declined. For details, see [Releasing a HarmonyOS App](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-app-0000002271695230).

#### ohos.permission.SYSTEM\_FLOAT\_WINDOW

Allows an application to be displayed in a floating window on top of other applications.

**Applicable scenarios and functionalities**:

-   Multi-party video call
-   Screen sharing
-   This permission is available only to PC/2-in-1 device applications.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/nmJP110CQMWEzGSQNvcyig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8DD48EF7422FE0F6B5604FF59B0DBC5181478B8FB000A6A194CDA2D48725A99)

For the window provided by a floating window, the application must also provide the user the way to exit.

**Alternative solution in other scenarios**: Use PiP. For details, see [Using PiP in Applications](../../../../../../application-framework/arkui/window-manager/using-pip-in-applications/document.md).

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 7

#### ohos.permission.READ\_CONTACTS

Allows an application to read **Contacts**.

**Applicable scenarios and functionalities**: The application needs to clone, back up, or sync contacts data.

**Alternative solution in other scenarios**: Use the Contacts Picker to access Contacts. For details, see [Contact Selection](../../../../../../application-services/contacts-kit/about-this-kit/document.md#contact-selection).

**Permission level**: system\_basic

**Authorization mode**: user\_grant

**Since**: 8

#### ohos.permission.WRITE\_CONTACTS

Allows an application to add, remove, and modify **Contacts**.

**Applicable scenarios and functionalities**: The application needs to clone, back up, or sync contacts data.

**Alternative for other scenarios**: Except for the preceding scenarios, applications are not allowed to modify contacts data. Instruct the users to modify contacts data in Contacts.

**Permission level**: system\_basic

**Authorization mode**: user\_grant

**Since**: 8

#### ohos.permission.READ\_AUDIO

Allows an application to access the audio files in a user directory.

**Applicable scenarios and functionalities**: The application needs to clone, back up, or sync audio files.

**Alternative for other scenarios**: Use AudioPicker to access audio files. For details, see [Selecting Audio Clips](../../../../../../application-framework/core-file-kit/user-files/selecting-and-saving-user-files/selecting-user-files/document.md#selecting-audio-clips).

**Permission level**: system\_basic

**Authorization mode**: user\_grant

**Since**: 9

#### ohos.permission.WRITE\_AUDIO

Allows an application to modify the audio files in a user directory.

**Applicable scenarios and functionalities**: The application needs to clone, back up, or sync audio files.

**Alternative for other scenarios**: Use AudioPicker to save audio files. For details, see [Saving Audio Clips](../../../../../../application-framework/core-file-kit/user-files/selecting-and-saving-user-files/saving-user-files/document.md#saving-audio-clips).

**Permission level**: system\_basic

**Authorization mode**: user\_grant

**Since**: 9

#### ohos.permission.READ\_IMAGEVIDEO

Allows an application to access the images/videos in a user directory.

Applicable scenarios and functionalities: The application needs to clone, back up, or sync images/videos.

**Alternative for other scenarios**: Use PhotoViewPicker to access user images or videos. For details, see [Selecting Media Assets Using Picker](../../../../../../media/media-library-kit/selecting-media-assets-using-picker/document.md).

**Permission level**: system\_basic

**Authorization mode**: user\_grant

**Since**: 9

#### ohos.permission.WRITE\_IMAGEVIDEO

Allows an application to modify the images/videos in a user directory.

**Applicable scenarios and functionalities**:

-   The application needs to clone, back up, or sync images/videos.
-   The application is a typical camera app that features photo shooting and recording scenarios.
-   The security control or authorization dialog box cannot be used to save images.

**Alternative for other scenarios**: Use a security component or authorization dialog box to save the media assets specified by the user to the Gallery. For details, see [Saving Media Assets](../../../../../../media/media-library-kit/saving-media-assets/document.md).

**Permission level**: system\_basic

**Authorization mode**: user\_grant

**Since**: 9

#### ohos.permission.READ\_WRITE\_DESKTOP\_DIRECTORY

Allows an application to access the **Desktop** directory and its subdirectories in the user directory.

Applicable scenarios and functionalities: This permission is available only to PC/2-in-1 device applications.

**Permission level**: system\_basic

**Authorization mode**: user\_grant

**Since**: 11

#### ohos.permission.ACCESS\_DDK\_USB

Allows extended peripheral drivers to access the USB DDK interfaces to implement development of USB extended peripheral drivers.

**Applicable scenarios and functionalities**:

-   The bus type of the external device to connect is USB. The external device connected can implement functions, such as fingerprint collecting, printing, and ID or fingerprint identification.
-   This permission is available only to PC/2-in-1 device applications.

Applications do not need to use this permission in other scenarios.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 11

#### ohos.permission.ACCESS\_DDK\_HID

Allows extended peripheral drivers to access the HID DDK interfaces to implement development of HID extended peripheral drivers.

**Applicable scenarios and functionalities**:

-   The application needs to access a HID device, such as a handwriting tablet, game controller, keyboard & mouse device.
-   This permission is available only to PC/2-in-1 device applications.

Applications do not need to use this permission in other scenarios.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 11

#### ohos.permission.READ\_PASTEBOARD

Allows an application to read **Pasteboard** data.

**Applicable scenarios and functionalities**:

-   This permission is available to PC/2-in-1 device applications.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/_Fq5eH9_T7ySBWlxZwkaSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22D6068B9F735C0FD2E2B87B01C0297FBECEED7509A35559E72729F9B0961CF2)
    
    -   By default, the system grants this permission for PC/2-in-1 device applications. However, users can change the permission settings on the Settings > Privacy & Security page.
    -   On the Settings page of PC/2-in-1 devices, users can choose between two options: Allow and Deny. Other devices offer three options: Always allow, Ask each time, and Deny.
    
-   The applications on other devices can request this permission only in the following scenarios:
    
    -   Bank applications need to read bank card numbers from Pasteboard to automatically generate cards.
    -   The application needs to read the password in a specific format from Pasteboard and automatically open the corresponding page in the application.
    -   Document editing applications.
    -   The system-level input method needs to read Pasteboard information to implement autofill. This permission is not available to built-in input methods of applications.

**Alternative for other scenarios**: Use PasteButton to read Pasteboard data. For details, see [Using PasteButton](../../../using-security-components/using-pastebutton/document.md).

**Permission level**: system\_basic

**Authorization mode**: user\_grant

**Since**: 11

#### ohos.permission.FILE\_ACCESS\_PERSIST

Allows an application to support persistent access to file URIs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/cK7IpL_ITKaHGQaCa_IbTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDE23ADD15CDA60CF3B18E66C8AF591648A661BE3C4C944BE35250C8956709CE)

The permission level of this permission has changed. After API 12, you still need to request this permission by following the procedure in [Requesting Restricted Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl).

**Permission level**: normal

**Authorization mode**: system\_grant

**Since**: 11

**Changelog**: The permission level is system\_basic in API version 11, and is changed to normal since API version 12.

#### ohos.permission.INTERCEPT\_INPUT\_EVENT

Allows an application to intercept input events.

**Applicable scenarios and functionalities**:

-   The application is a cloud desktop or remote login client, which needs to display the cloud computer of the remote server or the screen of the remote computer on a local device.
-   This permission is available only to PC/2-in-1 device applications.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 11

**Changelog**: The permission level is system\_core in API version 11, and is changed to system\_basic since API version 12.

#### ohos.permission.INPUT\_MONITORING

Allows an application to listen for input events.

**Applicable scenarios and functionalities**:

-   The application needs to record the on-screen information, and keyboard key events or the mouse pointer effect or touch effect need to be displayed during the screen recording process.
-   The application needs to share the screen.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 7

**Changelog**: The permission level is system\_core in API versions 7 to 11, and is changed to system\_basic since API version 12.

#### ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO

Allows an application to save images and videos to the user's directory within

up to 30 minutes after obtaining the permission. If it exceeds 30 minutes, a dialog box will be displayed again to request user authorization.

**Applicable scenarios and functionalities**:

-   The application, such as an HTML5 web page app, cannot use SaveButton.
-   Multiple images/videos cannot be saved at once in a save confirmation dialog.

**Alternative for other scenarios**: Use a security component or authorization dialog box to save the media assets specified by the user to the Gallery. For details, see [Saving Media Assets](../../../../../../media/media-library-kit/saving-media-assets/document.md).

**Permission level**: system\_basic

**Authorization mode**: user\_grant

**Since**: 12

#### ohos.permission.READ\_WRITE\_USER\_FILE

Allows an application to access and modify files in user directories.

**Applicable scenarios and functionalities**:

-   The IDE or debugging tool needs to read and write the user directory on the PC/2-in-1 device, for example, creating symbolic links or managing files in the user directory through a command-line tool.
-   This permission is available only to PC/2-in-1 device applications.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 13

#### ohos.permission.READ\_WRITE\_USB\_DEV

Allows an application to connect to a device and read and write the device data via USB for debugging purposes.

**Applicable scenarios and functionalities**:

-   The IDE or debugging tool needs to connect to a HarmonyOS device for development and debugging, for example, viewing the application logs on the device and performing profiling.
-   This permission is available only to PC/2-in-1 device applications.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 13

#### ohos.permission.GET\_WIFI\_PEERS\_MAC

Allows an application to obtain the MAC address of the peer Wi-Fi device.

This permission is required if you want to obtain the MAC address of the peer device when obtaining the Wi-Fi scanning result.

**Applicable scenarios and functionalities**: The IoT smart devices such as smart home devices and smart wearables needs to connect to the Internet.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 8

**Changelog**: The permission level is system\_core in API versions 8 to 13, and is changed to system\_basic since API version 14.

#### ohos.permission.SET\_TELEPHONY\_ESIM\_STATE\_OPEN

Allows a carrier application to add eSIM configuration files.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 13

**Changelog**: The permission level is **normal** in API versions 13 and **system\_basic** since API versions 14.

#### ohos.permission.kernel.DISABLE\_CODE\_MEMORY\_PROTECTION

Allows an application to disable its runtime code integrity protection.

**Applicable scenarios and functionalities**:

-   The application needs to modify the instruction content at runtime.
-   This permission is available only to applications on tablets, PCs and 2-in-1 devices.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 14

#### ohos.permission.kernel.ALLOW\_WRITABLE\_CODE\_MEMORY

Allows an application to apply for writable and executable anonymous memory.

**Applicable scenarios and functionalities**:

-   The just-in-time (JIT) compilation of the application's built-in engine is enabled. This permission cannot be used for hot updates.
-   Applications requesting this permission must adapt to the Secure Shield mode, ensuring no crashes occur in this mode.
-   This permission is available only to applications on tablets, PCs and 2-in-1 devices.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 14

#### ohos.permission.kernel.ALLOW\_EXECUTABLE\_FORT\_MEMORY

Allows an application to have its system JS engine to apply for anonymous executable memory with the MAP\_FORT identifier.

After the application has this permission, the system JS engine can request anonymous executable memory with MAP\_FORT for just-in-time (JIT) compilation, which increase the runtime execution efficiency.

**Applicable scenarios and functionalities**:

-   The game applications need to use the system engine to efficiently parse the game script.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 14

#### ohos.permission.MANAGE\_PASTEBOARD\_APP\_SHARE\_OPTION

Allows an application to set or remove the pasteable range of pasteboard data.

**Applicable scenarios and functionalities**:

-   The application needs to set or remove the range of Pasteboard data that can be pasted.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 14

#### ohos.permission.MANAGE\_UDMF\_APP\_SHARE\_OPTION

Allows an application to set or remove the sharing range of the data supported by the UDMF.

**Applicable scenarios and functionalities**:

-   The application needs to set or remove the UDMF data sharing scope.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 14

#### ohos.permission.ACCESS\_DISK\_PHY\_INFO

Allows an application to obtain the disk hardware information.

**Applicable scenarios and functionalities**:

-   This permission is available only to securities applications for securities and stock trading.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 15

#### ohos.permission.PRELOAD\_FILE

Allows an application to preload files to improve the file opening speed.

**Applicable scenarios and functionalities**: This permission is available only to document editing applications.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 15

#### ohos.permission.SET\_PAC\_URL

Allows an application to set the URL of the proxy auto config (PAC) script.

After the script address is configured, other applications can read and parse this script and determine whether to use a proxy based on the parsing result.

**Applicable scenarios and functionalities**:

-   Enterprise applications need to set an intranet proxy to manage enterprise traffic.
-   Government and public service applications and their trusted enterprise applications in China need to set a proxy to access secure websites.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 15

#### ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS

Allows a device administrator application to manage personal device restrictions.

**Applicable scenarios and functionalities:** This permission is available only to user as developer (UAD) applications.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 15

#### ohos.permission.START\_PROVISIONING\_MESSAGE

Allows an application to start the device management service deployment process, which activates the application as a personal device administrator application.

**Applicable scenarios and functionalities:** This permission is available only to user as developer (UAD) applications.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 15

#### ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER

Allows an application to use the fraud call log Picker to obtain call logs.

**Applicable scenarios and functionalities**:

-   This permission is available only to anti-fraud applications.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 15

#### ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER

Allows an application to use the fraud message Picker to obtain SMS messages.

**Applicable scenarios and functionalities**:

-   This permission is available only to anti-fraud applications.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 15

#### ohos.permission.PERSISTENT\_BLUETOOTH\_PEERS\_MAC

Allows an application to persist the virtual address corresponding to the MAC address of the peer Bluetooth device.

With this permission and the [access.addPersistentDeviceId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-access#accessaddpersistentdeviceid16) method, the application can persist the virtual address of the peer Bluetooth device obtained via BLE scanning, BR scanning, or listening for connections. The persistent virtual address can still be used even if Bluetooth is enabled or disabled, or the Bluetooth device is restarted.

**Applicable scenarios and functionalities**:

The application needs to connect to devices, such as smart home devices, smart wearables, and smart travel devices, through Bluetooth scanning to bind the user devices, and display device status or control devices.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 16

#### ohos.permission.ACCESS\_VIRTUAL\_SCREEN

Allows an application to manage virtual screens.

With this permission, the application can call APIs to perform virtual screen management, including creating, using, and destroying a virtual screen.

**Applicable scenarios and functionalities**:

The application needs to connect to a telematics device to play videos or use map navigation.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 16

#### ohos.permission.MANAGE\_APN\_SETTING

Allows an application to read or set APN information.

**Applicable scenarios and functionalities**:

The application needs to connect to the mobile data private network for office tasks.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 16

#### ohos.permission.GET\_WIFI\_LOCAL\_MAC

Allows an application to obtain the MAC address of the local Wi-Fi device.

**Applicable scenarios and functionalities**:

-   Securities trading such as stock, futures, and bond trading
-   Online banking services or identity authentication and signature verification
-   Applications running on PCs/2-in-1 devices

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 8

**Change history:** For API versions 8 to 15, this permission is available only to system applications. For API versions 16 and later, this permission is available to common applications on PCs/2-in-1 devices, and is available only to system applications on other devices.

#### ohos.permission.kernel.ALLOW\_USE\_JITFORT\_INTERFACE

Allows an application to call the JITFort API to update the content in MAP\_FORT.

**Applicable scenarios and functionalities**:

The application uses its own script engine and has JIT compilation enabled.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 16

#### ohos.permission.GET\_ETHERNET\_LOCAL\_MAC

Allows an application to obtain the current MAC address of the Ethernet.

**Applicable scenarios and functionalities**:

-   Securities trading such as stock, futures, and bond trading
-   Online banking services or identity authentication and signature verification
-   Applications running on PCs/2-in-1 devices

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 13

**Changelog**: This permission is available only to MDM applications in API version 13. From API version 14, this permission is available to normal enterprise applications. From API version 16, this permission is available to normal applications on PCs/2-in-1 devices, and is available only to system applications on other devices.

#### ohos.permission.kernel.DISABLE\_GOTPLT\_RO\_PROTECTION

Allows an application to disable the read-only protection on .got.plt.

**Applicable scenarios and functionalities**:

The basic capabilities that the application function depends on are not supported by the system. The .got.plt table must be modified to implement the application function. When applying for permissions, specify the reason why the system does not meet the requirements.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 17

#### ohos.permission.USE\_FRAUD\_APP\_PICKER

Allows an application to use the fraud app Picker to obtain application information.

**Applicable scenarios and functionalities**:

-   This permission is available only to anti-fraud applications.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 18

#### ohos.permission.ACCESS\_DDK\_DRIVERS

Allows a peripheral extension driver client to bind to the driver server.

This permission can be requested successfully only when:

1.  The target extension driver server in the value field of the permission declaration for the peripheral extension driver client has been launched or both the server and client have been launched.
2.  The capabilities provided by the target extension driver server comply with the requirements of the peripheral extension driver client.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Extra data**: Yes. For details about the configuration method, see [UI-based Driver Development](../../../../../hardware/driver-development-kit/basic-peripheral-driver-development/ui-based-driver-development/document.md#application-signing).

**Since**: 18

#### ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

Allows a peripheral extension driver to access the SCSI DDK APIs to implement development of SCSI extended peripheral drivers.

The APIs can be used to develop the following types of peripheral extension drivers:

Peripherals connected to the host via a USB bus and:

1.  InterfaceClass of the peripheral is Mass Storage (0x08) and InterfaceSubClass is SCSI Transparent Command Set (0x06).
2.  The peripheral can simulate a SCSI device in a way that is transparent to the operating system.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 18

#### ohos.permission.kernel.SUPPORT\_PLUGIN

Allows an application to install plugins.

**Applicable scenarios and functionalities**:

The application must have the related plugin mechanism to ensure that plugins can be used in accordance with the management regulations of the plugin market.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 19

#### ohos.permission.CUSTOM\_SANDBOX

Allows an application to set the sandbox type to dynamic sandbox.

**Applicable scenarios and functionalities**:

The permission is available only to Huawei internal development tools in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 18

#### ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

Allows an application to call the screen time guard APIs to restrict screen usage, apply application access control, and control the screen usage time.

**Applicable scenarios and functionalities**:

1.  Personal usage management: allowing users to monitor and control their own device and application usage, with the option to limit access to applications or screen time as needed for the purpose of focus, habit-building, and self-discipline
2.  Supervised usage management: enabling schools, parents, or organizations to oversee and manage the device and application usage of students, children, or employees, with the option to limit access to applications or screen time as needed for the purpose of protection, guardianship, and care

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Since**: 20

#### ohos.permission.CUSTOMIZE\_SAVE\_BUTTON

Allows an application to customize the icon and text of **SaveButton**.

**Applicable scenarios and functionalities**:

The default style provided by the saving control cannot meet business scenarios. The application needs to customize the icon and text of the saving control.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: general devices

**Since**: 20

#### ohos.permission.GET\_ABILITY\_INFO

Allows an application to query **Ability** information based on the URI or **FileType**.

**Applicable scenarios and functionalities**: This permission is available only to browser apps on PCs and 2-in-1 devices.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: PCs/2-in-1 devices

**Since**: 20

#### ohos.permission.ACCESS\_FIDO2\_ONLINEAUTH

Allows an application to use the Native Development Kit (NDK) of the passkey service.

**Applicable scenarios and functionalities**: The application needs to complete password-free authentication on web pages through the PassKey service.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: phones | PCs/2-in-1 devices | tablets

**Since**: 20

#### ohos.permission.USE\_FLOAT\_BALL

Allows an application to use the global float ball.

**Applicable scenarios and functionalities**:

1.  Identifying screen content and returning the data to the application for processing, enabling features such as cross-application searches, bill tracking, price comparison, and translation
2.  Tracking external data in real time for streamlined service processing, enabling features such as instant user inquiry response and financial market monitoring directly from the home screen

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: phones | tablets

**Since**: 20

#### ohos.permission.DLP\_GET\_HIDE\_STATUS

Allows an application to use the information hiding APIs to obtain the information hiding status.

With this permission, the application can obtain the current screen peeping state, that is, whether the screen is being peeped by others.

**Applicable scenarios and functionalities**:

The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: phones

**Since**: 18

**Changelog**: This permission is available only to system applications in API versions 18 to 19. From API version 20, it's also available to normal applications.

#### ohos.permission.READ\_LOCAL\_DEVICE\_NAME

Allows an application to obtain the local device name.

With this permission, the application can obtain the device name on the **About** screen in **Settings**. Without this permission, the application can only obtain the default device name.

**Applicable scenarios and functionalities**:

This permission is available only when the application needs to display the login device name during cross-device login via QR code scanning.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: phones | PCs/2-in-1 devices | tablets

**Since**: 20

#### ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM

Allows an application to request continuous tasks of special types, such as computing tasks.

**Applicable scenarios and functionalities**:

Automatic order receiving for merchant applications.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: general devices

**Since**: 20

#### ohos.permission.LINKTURBO

Allows an application to achieve multipath transmission.

With this permission, the application can initiate operations such as multi-network activation, monitoring, and release for multipath transmission.

**Applicable scenarios and functionalities**:

-   Multi-network traffic steering or redundant transmission in weak network environments for audio and video calls and conferences, games, online education, short and long videos, and live streaming, enhancing network anti-jitter performance and transmission reliability.
-   Transmission via multiple IP addresses when both the application and server support multi-network concurrency.
-   The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: phones | PCs/2-in-1 devices | tablets

**Since**: 20

#### ohos.permission.ACCESS\_NET\_TRACE\_INFO

Allows an application to detect the network and obtain the TraceRoute information to determine the possible causes of high network latency.

**Applicable scenarios and functionalities**:

Detecting network link quality or faults in network-based scenarios such as audio/video calls and conferences, games, online education, and live broadcasts that are sensitive to network latency.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: general devices

**Since**: 20

#### ohos.permission.READ\_WHOLE\_CALENDAR

Allows an application to read all calendar information.

**Permission level**: system\_basic

**Authorization mode**: user\_grant

**Since**: 9

**Changelog**: This permission is available only to system applications in API versions 9 to 19. From API version 20, it's also available to normal applications.

#### ohos.permission.WRITE\_WHOLE\_CALENDAR

Allows an application to add, remove, or change all calendar events.

**Permission level**: system\_basic

**Authorization mode**: user\_grant

**Since**: 9

**Changelog**: This permission is available only to system applications in API versions 9 to 19. From API version 20, it's also available to normal applications.

#### ohos.permission.SET\_SYSTEMSHARE\_APPLAUNCHTRUSTLIST

Allows an application to set the trustlist of target applications for system sharing.

With this permission, the application can choose the target applications for system sharing.

**Applicable scenarios and functionalities**:

1.  The permission is available only when the host application needs to control the scope of target applications for system sharing.
2.  The permission is available only to the enterprise applications in the allowlist. To add your application to the allowlist, contact enterprise technical support.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: phones | PCs/2-in-1 devices | tablets

**Since**: 21

#### ohos.permission.HOOK\_KEY\_EVENT

Allows an application to intercept keyboard input events.

With this permission, the application can integrate its custom key handling process into the system's key handling process prior to the key event being dispatched to the application window.

**Applicable scenarios and functionalities**:

-   Securities login or trading, such as stock, futures, and bond trading
-   Online banking transaction or identity authentication: online banking services (such as online banking login, transfer, and remittance), or password control tools for identity authentication for online banking users

**Permission level**: system\_basic

**Authorization mode**: manual\_settings

**Supported devices**: PCs/2-in-1 devices | tablets

**Since**: 21

#### ohos.permission.WEB\_NATIVE\_MESSAGING

Allows an application to use the web native messaging capability.

With this permission, the application can enable communication between browser extensions and local applications.

**Applicable scenarios and functionalities**:

Browser-type applications where users need to access web pages and browse Internet resources by entering URLs

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Supported devices**: PCs/2-in-1 devices

**Since**: 21

#### ohos.permission.SUBSCRIBE\_NOTIFICATION

Allows an application to read notifications published by the system or installed applications.

**Applicable scenarios and functionalities**:

Wearable applications used by smart watches that can display notifications

With this permission, the application can read notifications published by the system or installed applications, and then forward these notifications to the corresponding watch through short-range communication protocols such as Bluetooth to display the notifications.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: phones | tablets

**Since**: 22

#### ohos.permission.CUSTOM\_SCREEN\_RECORDING

Allows an application to record the screen without displaying any pop-up.

With this permission, the application can record the screen without showing a privacy pop-up each time recording is initiated.

**Applicable scenarios and functionalities**:

\- Applications that support screen recording triggered via a UI component

\- Applications that support remote login and can display the remote login screen on a local device

\- Applications that support desktop sharing and can share the local device's screen with other devices

**Permission level**: system\_basic

**Authorization mode**: manual\_settings

**Supported devices**: PCs/2-in-1 devices

**Since**: 22

#### ohos.permission.GET\_IP\_MAC\_INFO

Allows an application to obtain the IP address and MAC address of a network device.

**Applicable scenarios and functionalities**:

network connection or identification (not applicable to device location)

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: general devices

**Since**: 22

#### ohos.permission.ACCESS\_USER\_FULL\_DISK

Allows an application to access the public user directory without a pop-up.

With this permission, the application can access the public directory without having to notify the user via a pop-up every time.

**Applicable scenarios and functionalities**:

\- Remote login client applications: display of the remote device screen on a local device

\- Antivirus applications: full-disk virus scan and removal

**Permission level**: system\_basic

**Authorization mode**: manual\_settings

**Supported devices**: PCs/2-in-1 devices

**Since**: 22

#### ohos.permission.kernel.LOAD\_INDEPENDENT\_LIBRARY

Allows an application to load shared libraries signed with binary certificates.

**Applicable scenarios and functionalities**:

This permission is open to Huawei ecosystem development tools.

**Risk description**: This permission allows the loading of unreviewed code, which may affect the application security. Therefore, exercise caution when using this permission.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Supported devices**: PCs/2-in-1 devices

**Since**: 20

**Changelog**: This permission is available only to system applications in API versions 20 to 21. From API version 22, it's also available to normal applications.

#### ohos.permission.CRYPTO\_EXTENSION\_REGISTER

Allows an application to register and deregister the crypto extension.

**Applicable scenarios and functionalities**:

-   UKey developers.
-   Banking and financial applications with UKey vendor collaboration certification.

**Permission level**: system\_basic

**Authorization mode**: system\_grant

**Device**: PCs/2-in-1 devices

**Since**: 22
