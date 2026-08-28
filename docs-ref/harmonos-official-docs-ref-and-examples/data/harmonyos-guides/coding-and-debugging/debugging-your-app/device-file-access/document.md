# Device File Access

DevEco Studio provides Device File Browser that simplifies file management on connected devices. You can create, delete, upload, and download files on the target device without using any CLI. Currently, Device File Browser offers two views: file view and app sandbox view.

#### Scenarios

-   Display the file list and basic file information of a device.
-   Search for a file or folder on a device.
-   Create or delete files on a device.
-   Upload files from the local PC to a device or download files from a device to the local PC.

#### Constraints

-   Devices can be connected using a USB cable or via Wi-Fi.
-   Unauthorized access to directories is not supported. Permissions are required for creating, deleting, uploading, and downloading files on a device.
-   Files cannot be dragged.
-   File modification on the device is not supported. If you need to modify a file, download it to the PC, modify the file locally, and upload the modified file to the device.
-   Shortcuts to files or folders cannot be uploaded.
-   The app sandbox view is not compatible with emulator devices.
-   To use the app sandbox view for inspecting the file structure and performing operations like adding, deleting, uploading, or downloading within the app sandbox, the app must be a debug app.

#### Procedure

1.  On the menu bar, choose **View** > **Tool Windows** > **Device File Browser** to start Device File Browser.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/T9gAS8-CSEiDmGGP2-h_OQ/en-us_image_0000002500910232.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C2F5509449849EBD37EACE037CED0122095042BFD0F1445E37DD94138601382)
    
2.  Select a device from the drop-down list box.
3.  After you select a device, the file/folder list of the device is displayed. You can perform the following operations:
    
    1.  Create or delete a file or folder.
    2.  Transfer files between the local PC and the device. To download a file or folder to the local PC, right-click the file or folder and choose **Save As**. To upload a file to the device, right-click the file on the local PC and choose **Upload**.
        
        To view a database file, you can download the database file (for example, **data > app > el2 > 100 > database > _Project name_ > entry > rdb > _File name_**) to the PC and use other tools to view the file.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/QEY1afZhTD68s9TLlZqP_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF5D79BEA24819E73426ABB87C81E1485B46C7B841CC0545972188FA7278D47A)
        
        Since DevEco Studio 6.0.0 Beta2, you can press **Ctrl/Shift+left mouse button** (**Command/Shift+left mouse button** on macOS) to select multiple files or folders and download them to the local computer.
        
    3.  Enter a keyword in the Device File Browser text box to search for a file.
    4.  Double-click a file to open it on DevEco Studio. The file opened is downloaded to a temporary directory (**%USER%\\AppData\\Local\\Huawei\\DevEcoStudio{_Version number_}\\device-file-browser\\{_Device name_}\\{_File path on the device_}**) by default. After the file is closed, the temporary file will be automatically deleted.
    5.  If a file is uploaded to the device using a command, you need to right-click the folder and choose **Synchronize** from the shortcut menu. Then, the file can be displayed in the **Device File Browser** window.
    

#### Accessible Directories

Device File Browser provides access to the following directories: [app sandbox directory](../../../application-framework/core-file-kit/application-files/application-sandbox/document.md), temporary directory, log directory, public directory, and media library directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/2IPkRmJxTtS0DrCrlhAvcw/en-us_image_0000002501637960.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B961B8056194164F4749F17A4A1EB53B5633A0CB52411672F973A890893C0AC8)

## App Sandbox Directory

The app sandbox directory is where data and resource files related to the app are stored. You can access this directory in two ways:

-   **File view**
    
    The file view displays the file structure of the current device as it exists on the device according to the device's actual physical paths.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/S6nkdZ0nTH-2H7jTU-vXNQ/en-us_image_0000002532670155.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6E567E82964DD314280D01EC7E6D8EC8A1EEC9DD42BC0D420499CD2E1576C89)
    
    The physical path of the app sandbox on the device is **/data/app/{el1,el2}/100/{base,database}/{_packageName_}**.
    
    Under the file view, files in the **el1** directory are read-only, while files in the **el2** directory can also be downloaded, but no other operations are allowed.
    

-   **App sandbox view**
    
    The app sandbox view displays the structure of all debug apps within their respective sandboxes.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/DB2SKPTvSfyj7o37cxNXSw/en-us_image_0000002532670151.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A3804216645B9E31A62BAC0E552221B061DA369FCFB2DC1AA89E0FE7849E90B)
    
    To view the file structure of an app using the sandbox view on API versions earlier than 15, you must configure the **ohos.permission.INTERNET** permission to enable Internet access within the **module.json5** file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/H8qc1BNxTg-RbMmRd7dmmA/en-us_image_0000002501070076.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=805E3A78C3BF29B03556CA2CD547A28526BF97AF0541226EEF119F33DEA182D0)
    
    The sandbox path is **/data/storage/{el1,el2}/{base,database}**, which corresponds to the physical path.
    
    Under the app sandbox view, files in both the **el1** and **el2** directories can be created, deleted, uploaded, and downloaded.
    

## Temporary Directory

The temporary directory, at **/data/local/tmp/**, is used to store temporary files generated during debugging and testing. You can create, delete, upload, and download files in this directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/HNiv1-AvS-WrKitKt50YbQ/en-us_image_0000002532670153.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E963375CF1E4E8758259910527E17105B69EA93E8AC076007BFF3CC4090AA12)

## Log Directory

When your app is running, logs are generated in real time using HiLog and stored in the HiLog output buffer, which is typically 256 KB. When the buffer reaches its capacity, historical logs are saved as compressed packages in the **/data/log/hilog/** directory.

To view historical logs, download the compressed packages and the **hilog\_dict.XXX.zip** file (data dictionary file) in the directory, and then use the [hilogtool](../../../system/debugging-tools/debugging-commands/hilogtool/document.md) to parse the log files.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/lZc25HNhQfuDa4_GQGydVw/en-us_image_0000002501070088.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5A9CE5D328F16A0613AD63DADC1E5746F48B525AEAD607B360B7F3986CF7B1A)

## Public Directories

The public directories, such as **Desktop**, **Documents**, and **Downloads**, are at **/storage/media/100/local/files/Docs**. You can delete, upload, and download files in these directories.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/KuUroCW2SIm65Dl-2GnaFA/en-us_image_0000002501070094.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=816149B3B819AA03F625C6FB39D178DC7FC43ABCDFBFEC484714637F86EE5F6B)

## Media Library Directory

Since API version 22, the media library directory **/mnt/data/100/media\_fuse/Photo** has been added. The original directory **/storage/media/100/local/files/Photo** is now a symbolic link that redirects to **/mnt/data/100/media\_fuse/Photo**. This new directory supports uploading, downloading, and deleting image and video files.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/ZeF-zW__T26pJV254ec16g/en-us_image_0000002533342953.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41922E57E1693D688A1431440F114372D6C44F9FB5A985A173082C9D220CD674)

#### Special Directories

There are two special directories on the device: **faultlog** and gallery directories. These directories are not displayed in Device File Browser, but can be accessed using hdc commands.

## faultlog Directory

When an app crashes, a crash log is generated and saved in **/data/log/faultlog/faultlogger**. While you cannot view this directory directly in Device File Browser, you can access and export its contents using hdc commands.

1.  To query the crash log list:
    -   For devices running versions earlier than 5.1.0.54:
        
        hdc shell hidumper -s 1201 -a "-p Faultlogger"
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/6An60cJdRTiFjgDk01azyQ/en-us_image_0000002501070078.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4645CF39ABD28AF06A6ABB6BAA2C06F83F6B74555FC743F3CDD85938B30D8AF)
        
    -   For devices running 5.1.0.54 or later (the timestamp includes milliseconds):
        
        hdc shell hidumper -s 1201 -a "-p Faultlogger %s -LogSuffixWithMs"
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/_ib_ovVDRuaihr7DZIiNKg/en-us_image_0000002501070080.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8C521F4F52BE2B5F8E9A7A1C01229BF2A6BF4BC7DAB0C8350AA4F155CBD4740)
        
2.  To view a specified crash log file:
    
    hdc shell hidumper -s 1201 -a "-p Faultlogger -f {filename}"
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/-03K3nPcSH25KZ_n8n5Sng/en-us_image_0000002501070082.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE37F0AE2A1CEF456457A61A289F181BF7484935D8413C95F840DF5E51309BB7)
    
3.  To download the log file to the specified path on your local PC:
    
    hdc file recv /data/log/faultlog/faultlogger/{filename} {path}
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/_V6zkOUTRYCqswycfyJwaQ/en-us_image_0000002532670169.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AF7B2092AD3461EB6AAEF435F6C82DEDAD335BF3C69B9D4D2DACA0CC00B4EFA)
    

## Gallery Directory

The gallery directory stores image and video files generated by system apps, such as the screen recorder and camera. To download these files to your local PC, perform the following:

1.  View the file name and extension of the desired media file, for example, **a.mp4**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/-hC0NFr9Re6KYmWFCPkx6g/en-us_image_0000002532670167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78CDDDF286CBAFD1365689A933CE970831E647503BBD0ACF1FE058A09DB19779)
    
2.  Query the file path and record it as {FilePath}.
    
    hdc shell mediatool query a.mp4 -u
    
    -   If the query result contains the **uri** field, the file path (on the third line of the result) cannot be directly used for download.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/0PtGUo8GRcK66-vDBUP4VQ/en-us_image_0000002532670159.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84CAD031C772D2937FCB8E3A8C1A9445FCB6D89585AD9024989F0DF341D72176)
        
        In this case, use the value of **uri** to save the file to a path on which you have the download permission, for example, **/data/local/tmp**:
        
        hdc shell mediatool recv file://media/Photo/2/VID\_1744944984\_000/a.mp4 /data/local/tmp
        
        The second line in the output is the downloadable file path.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/3UPmsoatQwGznYAmSkmlCA/en-us_image_0000002500910240.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADEB5E09499D6E7CDDF00F642C1EBEB2DC5D0A91A277E32ADD64E68369C0B912)
        
    
    -   If the query result does not contain the **uri** field, the downloadable file path is listed on the second line of the output.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/GQonOIyDSOKUEZEQcsI9hg/en-us_image_0000002501070090.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5CADE18E4A671B8E71E604284F7E6309766663D4394D4E58E837FCF62CCF120)
        
3.  Use the downloadable file path to download the file to your local PC.
    
    hdc file recv {FilePath} .\\
    

#### Accessing the App Sandbox in CLI Mode

You can access the [sandbox directory](../../../application-framework/core-file-kit/application-files/application-sandbox/document.md#mappings-between-application-sandbox-paths-and-physical-paths) of debug apps through the CLI.

-   Since API version 15, you are advised to use the hdc tool to access the sandbox directory of your debug app. For details about hdc, see [hdc](../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md).
    1.  Start the app on the device.
        
        $ hdc shell aa start -a {abilityName} -b {bundleName}
        start ability successfully.
        
        -   **abilityName**: ability name of the app.
        -   **bundleName**: name of the app bundle to debug.
        
    2.  Run commands to access the app sandbox directory, create directory files, and delete files in the specified directory.
        
        $ hdc shell -b {bundleName} ls -lZ -A "./data/storage/el2/base"          // List files in the app sandbox /el2/base directory (return full file information).
        $ hdc shell -b {bundleName} ls -A "./data/storage/el2/base"          // List files in the app sandbox /el2/base directory (return only file names).
        $ hdc shell -b {bundleName} mkdir -p "./data/storage/el2/base/test"     // Create a test directory under the app sandbox /el2/base directory.
        $ hdc shell -b {bundleName} rm -r "./data/storage/el2/base/test.txt"  // Delete the test.txt file under the app sandbox /el2/base directory.
        $ hdc shell -b {bundleName} rm -r "./data/storage/el2/base/test"      // Delete the test directory under the app sandbox /el2/base directory.
        
    3.  Run commands to send files to the app sandbox directory and download files from the sandbox to the local PC.
        
        $ hdc file send -b {bundleName} "D:\\test.txt" "./data/storage/el2/base"    // Send the file to the device sandbox /el2/base directory.
        $ hdc file recv -b {bundleName} "./data/storage/el2/base/test.txt" D:\\  // Download the file from the device sandbox /el2/base directory to the local PC.
        
-   For versions earlier than API version 15, perform the following to access the sandbox directory of your debug app:
    1.  Add the Internet access permission to the **module.json5** file of the entry module.
        
        "requestPermissions": \[
          {"name":  "ohos.permission.INTERNET"}
        \]
        
    2.  Launch the bftpd service for the app on the device and check whether the service has started successfully on the specified port:
        
        $ aa process -b {bundleName} -a {abilityName} -p "/system/bin/bftpd -D -p {port}"  -S
        start native process successfully.
        $ ps -ef | grep bftpd
        20020143     12254   613 0 11:52:53 ?     00:00:00 bftpd -D -p 9021   // The bftpd service starts successfully on the corresponding port.
        shell        13035 11901 10 11:54:44 ?    00:00:00 grep bftpd
        
        -   **bundleName**: name of the app bundle to debug.
        -   **abilityName**: ability name of the app.
        -   **port**: available port number.
    3.  Run commands to access the app sandbox directory, create directory files, and delete files in the specified directory.
        
        $ ftpget -p {port} -P guest -u anonymous localhost -l /data/storage/el2/base           // List files in the app sandbox /el2/base directory (return full file information).
        $ ftpget -p {port} -P guest -u anonymous localhost -L /data/storage/el2/base           // List files in the app sandbox /el2/base directory (return only file names).
        $ ftpget -p {port} -P guest -u anonymous localhost -M /data/storage/el2/base/test      // Create a test directory under the app sandbox /el2/base directory.
        $ ftpget -p {port} -P guest -u anonymous localhost -d /data/storage/el2/base/test.txt  // Delete the test.txt file under the app sandbox /el2/base directory.
        $ ftpget -p {port} -P guest -u anonymous localhost -D /data/storage/el2/base/test      // Delete the test directory under the app sandbox /el2/base directory (only empty directories can be deleted).
        
    4.  Run the command to send files to the app sandbox directory and download files from the sandbox to the local device. (**/data/local/tmp/** is used as a transit directory.)
        
        $ hdc file send test.txt /data/local/tmp/test.txt    // First, send the file to the data/local/tmp directory on the device.
        $ ftpget -p {port} -P guest -u anonymous localhost -s /data/local/tmp/test.txt /data/storage/el2/base/test.txt  // Then, push it to the app sandbox directory.
        $ ftpget -p {port} -P guest -u anonymous localhost -g /data/local/tmp/test.txt /data/storage/el2/base/test.txt  // First, download the file to the data/local/tmp directory on the device.
        $ hdc file recv /data/local/tmp/test.txt test.txt  // Then, obtain it from the device.
        

#### FAQs

What should I do if opening a folder in the app sandbox view displays the "\[Fail\]\[E003001\] Invalid bundle name" message?

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/f3thZVxGQQepxp0Ht-GTYQ/en-us_image_0000002532750103.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C212A7431D15B30E5954204C5DC5818FA566F632F32BDEA18CFB0EBA83587915)

Follow the steps below to troubleshoot:

1.  Check whether the app is a debug app. Only debug apps support sandbox file access.
2.  Check whether the app has been launched at least once. If the app has not been run yet or the device was restarted after installation, the app sandbox may not be mounted. To fix the issue, run the app and then right-click the target folder in Device File Browser and choose **Synchronize**.
