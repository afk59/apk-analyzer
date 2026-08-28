# About This Kit

Core File Kit provides capabilities for accessing and managing application files and user files. You can use the APIs provided by Core File Kit to manage, search for, and back up different types of files efficiently.

#### Overview

In Core File Kit, the files are classified into the following types based on the file owner:

-   [Application files](../application-files/application-file-overview/document.md): files of an application, including the installation files, resource files, and cache files of the application.
    
-   [User files](../user-files/user-file-overview/document.md): files of a user who has logged in to the device. User files include the user's images, videos, audio clips, and documents.
    
-   System files: files irrelevant to applications and users. System files include public libraries, device files, and system resource files. The system files do not need to be managed by developers and are not described in this document.
    

The file systems can be classified into the following types based on the file storage location (location of the data source):

-   Local file system: allows access to the files stored on a device and its external storage devices (such as USB flash drives and removable hard drives). The local file system is the most basic file system and is not described in this document.
    
-   [Distributed file system](../distributed-file-system/distributed-file-system-overview/document.md): allows access to files across devices, which include not only the local device and its external storage devices, but also the devices connected over a computer network.
    

**Figure 1** File classification model

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/ojh5R3xgRkuXOB-Vwbdp6w/en-us_image_0000002568764769.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061950Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C3E289B91067B5BD4B663193A76A4A1B86B4425CF9EC139934EC6A2BA798E52)

#### When to Use

You can use Core File Kit in any of the following scenarios:

-   Access to and share of application files
-   Backup and restore of application data
-   Operations for selecting and saving user files
-   Cross-device file access and sharing

#### Available Capabilities

-   Accessing application files, including viewing, creating, reading, writing, delete, moving, and copying an application file, and obtaining attributes of an application file.
-   Uploading application files to a network server and downloading network resource files from a network server to the local application file directory.
-   Obtaining the storage space of an application, and the total and available space of a file system.
-   Sharing application files to other applications and using the files shared by other applications.
-   Accessing the data backup and restore framework to customize data backup and restore behaviors, such as whether to allow backup and restore and specifying the data to be backed up, by modifying the configuration file.
-   Accessing and managing user files with the [user file access framework](#user-file-access-framework). For example, selecting and saving user files.
-   Accessing and copying files across devices.

#### Features

-   Sandbox isolation:

Each application has a dedicated [sandbox directory](../application-files/application-sandbox/document.md) in the internal storage. The sandbox directory is a collection of the [application file directory](../application-files/application-sandbox/document.md#application-file-directory-and-application-file-path) and the system files required for application running. The sandbox feature stands out with the following advantages:

-   Isolation: The application sandbox provides a completely isolated environment to ensure secure access to application files.
    
-   Security: The application sandbox defines the minimum data visible to each application, which protects application file security.
    
-   Application share:
    

Files can be shared between applications by uniform resource identifier (URI) or file descriptor (FD). The application share feature has the following advantages:

-   Portability: Files can be easily shared between applications, without the need for the user to switch between different applications.
-   High efficiency: Files can be quickly transferred between applications, which eliminates redirections and the response time.
-   Data consistency: File share between applications ensures data integrity and consistency, preventing data corruption or loss during transmission.
-   Security: File share between applications prevents files from being illegally obtained or tampered with. In addition, authorized file access further enhances file security.

#### Working Principles

## Application File Access Framework

The application file access framework is implemented through [ohos.file.fs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs). You do not need to care about the internal implementation. For details about the basic file operation APIs, see [Available APIs](../application-files/application-file-access-and-management/accessing-application-files-arkts/document.md#available-apis).

## User File Access Framework

You can use the user file access framework to access and manage user files. This framework leverages the ExtensionAbility of HarmonyOS to provide a set of methods and interfaces for accessing user files.

**Figure 2** User file access framework

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/T1i2ocYqRPynU9mbR4H6OQ/en-us_image_0000002537765044.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061950Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D895C6711B000A62E4CD97E237BCBB32FFFAEA6ECCB9CA086ED5AC9D48DC98C8)

-   The file access client (a system application or third-party application) can access user files, for example, select a photo or save multiple documents, by starting the **FilePicker** application.
    
-   **FilePicker**: a system prebuilt application that allows a client to select and save user files without any permission. For details, see [Selecting User Files](../user-files/selecting-and-saving-user-files/selecting-user-files/document.md).
    
-   **FileManager**: You can also develop your own file picker or file manager application as required. This function is available only for system applications. (
    
-   The user file access framework provides the following functional modules:
    
    -   **File Access Helper**: provides APIs for the **FileManager** and **FilePicker** to access user files.
    -   **File Access ExtensionAbility**: implements file access via the following services:
        -   **UserFileManager**: implements management of the files on the built-in storage based on the File Access ExtensionAbility framework.
        -   **ExternalFileManager**: implements management of the files on the external storage based on the File Access ExtensionAbility framework.

#### Related Kits

Ability Kit: The user file access framework of Core File Kit depends on the Extension capability provided by Ability Kit and is scheduled and managed by Ability Kit.
