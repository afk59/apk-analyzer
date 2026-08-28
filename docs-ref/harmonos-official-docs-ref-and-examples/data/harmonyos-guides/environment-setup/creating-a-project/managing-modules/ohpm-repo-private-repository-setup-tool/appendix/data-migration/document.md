# Data Migration

ohpm-repo 2.2.0 and later versions support data migration. In the ohpm-repo configuration file, **db** is used to configure metadata storage, and **store** is used to configure file storage. When being used together, **db** and **store** must comply with the specifications in the following table. To change the storage mode of **db** and **store**, you need to migrate data.

| 
db: Metadata Storage

 | 

Corresponding store Type: Third-party File Storage

 |
| :-- | :-- |
| 

FileDB

 | 

File storage

 |
| 

MySQL (supported since ohpm-repo 1.1.0)

 | 

File storage, SFTP storage (supported since ohpm-repo 1.1.0), custom storage (supported since ohpm-repo 2.2.0)

 |

#### Procedure Overview

1.  [Back up data](../data-backup/document.md) to prevent any loss.
2.  Upgrade ohpm-repo to the target version by referring to [Version Upgrade](../version-upgrade/document.md).
3.  [Export data using migration commands](#section397615294129).
4.  Modify the storage modes of **db** and **store** in the configuration file and [restart ohpm-repo in the new storage mode](#section1959530132115).
5.  [Import data using migration commands](#section17126124310255).

#### Backing Up ohpm-repo Data

For details, see [Data Backup](../data-backup/document.md).

#### Upgrading ohpm-repo to the Latest Version

For details, see [Version Upgrade](../version-upgrade/document.md).

#### Exporting Data Using Migration Commands

1.  Export DB data.
    
    Run the [export\_userinfo](../../related-commands/data-migration-commands/ohpm-repo-export-userinfo/document.md) command to export data from the following data tables and export the encryption components. The command will automatically package these outputs into an **export\_userInfo\__xxx_.zip** file in the command execution directory.
    
    -   user
    -   group\_member
    -   public\_key
    -   access\_token
    -   uplink
    -   uplink\_proxy
    -   repo
    -   repo\_permission
    -   validation\_config
    -   system\_security
    
    ohpm-repo export\_userinfo
    
    PS D:\\> ohpm-repo export\_userinfo
    \[2025-08-09T19:14:16.721\] \[INFO\] default - initialize "file database" successfully.
    ...
    \[2025-08-09T19:14:16.734\] \[INFO\] default - export the "system\_security" table done.
    \[2025-08-09T19:14:16.761\] \[INFO\] default - userinfo exported completed, save the .zip file to : "D:\\export\_userInfo\_1754738056722.zip".
    
2.  Export the list of released packages.
    
    Run the [export\_pkginfo](../../related-commands/data-migration-commands/ohpm-repo-export-pkginfo/document.md) command to export the list of released packages.
    
    ohpm-repo export\_pkginfo
    
    PS D:\\> ohpm-repo export\_pkginfo
    ...
    \[2025-08-09T17:56:15.319\] \[INFO\] default - export matched packages success: save to "D:\\pkgInfo\_1754733375315.json".
    
3.  Download package files in batches.
    
    Run the [batch\_download](../../related-commands/data-migration-commands/ohpm-repo-batch-download/document.md) command to download package files in batches from the **store** storage directory configured in ohpm-repo.
    
    Use the **pkgInfo\__xxxx_.json** file generated in Step 2 as the [batch\_download](../../related-commands/data-migration-commands/ohpm-repo-batch-download/document.md) command parameter to download HAR or TGZ packages in batches and generate the **batch\_download\__xxx_.zip** file in the command execution directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/iv-ybzO0TIWq1br4eRr3fw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C20EA853EB92DB3B61EDBF81377BBC756FCE3B24D757BA95CCF8B211A7E20D3)
    
    If you want to download only some of the packages, delete the packages that you do not want to download from the **pkgInfo\__xxxx_.json** file generated in Step 2.
    
    ohpm-repo batch\_download <pkgInfo\__xxxx_.json _address_\>
    
    PS D:\\> ohpm-repo batch\_download D:\\pkgInfo\_1754733375315.json
    \[2025-08-09T18:33:30.349\] \[INFO\] default - download "@ohos/test@1.0.0" from repository "ohpm" successfully".
    \[2025-08-09T18:33:30.367\] \[INFO\] default - download "@ohos/test-two@1.0.0" from repository "ohpm" successfully".
    ...
    \[2025-08-09T18:33:30.466\] \[INFO\] default - all "6" package(s) are successfully download.
    \[2025-08-09T18:33:30.466\] \[INFO\] default - save the .zip file to : "D:\\batch\_download\_1754735610304.zip".
    \[2025-08-09T18:33:30.467\] \[INFO\] default - Clear the cache.
    
    The **batch\_download\__xxx_.zip** file contains a directory named after the repository. Within this directory, the **pkgInfo.json** file is located, which contains metadata for each package, including its file name, package name, organization, uploader, and tag. It is used during batch upload to accurately assign the real uploader (a specific user in the ohpm-repo database) to each package, and the package's tag information is also uploaded.
    
4.  Export the package permission data.
    
    Since ohpm-repo 5.4.0, the package permission data can be exported using the [export\_pkgPermission](../../related-commands/data-migration-commands/ohpm-repo-export-pkgpermission/document.md) command.
    
    ohpm-repo export\_pkgPermission
    
    PS D:\\> ohpm-repo export\_pkgPermission
    ...
    \[2025-09-16T14:58:24.806\] \[INFO\] default - successfully exported all package permissions: saved to "D:\\packagePermission\_1758005904806.json".
    

#### Restarting ohpm-repo in the New Storage Mode

Open the **config.yaml** configuration file in the root directory of the ohpm-repo package, modify the **db** and **store** configuration options, and specify the required storage mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/GxBkFAx6Tx-tHcMus8L1Uw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8394A25963B6C222716DAB1FDC1EEFA5D3F09D295477FA91C6005A5053B30CE)

After modifying the **db** and **store** configuration options, you need to configure the new **<_deploy\_root_\>** directory in the configuration file.

Use the modified configuration file to run the installation command again. (This step is mandatory to initialize the database and other necessary configurations.)

ohpm-repo install --config <_configuration file path_\>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/EV6Acb8mTTK_l86RMADTGw/en-us_image_0000002532668827.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2334870312D1C5D9B4DACE07BB4E30399EAA63E37581E60145F0C4BCFA289A79 "Click to enlarge")

Update the environment variables as prompted and restart ohpm-repo.

ohpm-repo start

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/EIzMxBhBSpO3ouZYWdV9TQ/en-us_image_0000002501068770.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EB654F2C19192BBA6684C1B917A8C531E9F3551E81FC27E4D1236226BF50A00 "Click to enlarge")

#### Importing Data Using Migration Commands

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/pSBBGLZ7TfuEmLgXXCnb-g/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CE0784D066DC62EE6E22CFFBEB50A7C401DBDF7952CA51841423F3144664DE5)

-   For deployment on a new host, transfer the **export\_userInfo\__xxx_.zip**, **batch\_download\__xxx_.zip**, and **packagePermission\__xxx_.json** files exported from ohpm-repo to the target host.
-   Import the DB data first and then upload the data in batches to avoid errors caused by the failure to find the corresponding user and organization during the upload.

1.  Stop the ohpm-repo service.
    
    Stop the ohpm-repo service before starting data migration to prevent data exceptions caused by user access during the migration.
    
2.  Import DB data.
    
    Run the [import\_userinfo](../../related-commands/data-migration-commands/ohpm-repo-import-userinfo/document.md) command to import data in **export\_userInfo\__xxx_.zip** to the database.
    
    ohpm-repo import\_userinfo <zip\_file> --clean-db
    
    PS D:\\> ohpm-repo import\_userinfo D:\\export\_userInfo\_1754738056722.zip --clean-db
    \[2025-08-09T19:19:31.623\] \[INFO\] default - verifying the validity of the meta crypto component.
    \[2025-08-09T19:19:31.633\] \[INFO\] default - the meta crypto component is verified successfully.
    \[2025-08-09T19:19:31.639\] \[INFO\] default - initialize "file database" successfully.
    \[2025-08-09T19:19:31.660\] \[INFO\] default - all database data has been cleaned.
    \[2025-08-09T19:19:31.660\] \[INFO\] default - importing data in the 'user.json' file.
    ...
    \[2025-08-09T19:19:31.673\] \[INFO\] default - importing data in the 'system\_security.json' file.
    \[2025-08-09T19:19:31.674\] \[INFO\] default - data import finished.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/sN5k7xCfQd6GNhKKOWucIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=786564C5989E7A7BACC361F36B342C9FD8497F7006A4465AA0B466AB30910833)
    
    1.  **\--clean-db** indicates that all table data will be cleared before data import, including the **admin** user generated by default when ohpm-repo is started.
    2.  If **\--clean-db** is not configured, duplicate data may exist during the import. By default, the system skips other duplicates except the first one in compatible mode. For example, there are two **admin** users. The original **admin** user in the database is referred to as A1, and the **admin** user in the imported data is referred to as A2. By default, A1 is retained. If the ID of A2 exists in other tables to be imported, it will be replaced with the ID of A1 in advance. Note that you need to use the password of A1 to log in.
    
    After the data is imported, you can start the ohpm-repo service and log in to the management page for verification.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/eJbNr0LzSoqisYlPsG1BdA/en-us_image_0000002532748797.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8359D757B2A3AEA4F1C390A22C8FF8CDDFB6FACC34C5DEAA86A8342AEE885C53 "Click to enlarge")
    
3.  Upload packages in batches to the **store** directory configured for the ohpm-repo.
    
    Run the [batch\_publish](../../related-commands/data-migration-commands/ohpm-repo-batch-publish/document.md) command to release the packages in **batch\_download\__xxx_.zip**, which is generated during batch download, to ohpm-repo in sequence.
    
    ohpm-repo batch\_publish <zip\_file>
    
    PS D:\\> ohpm-repo batch\_publish D:\\batch\_download\_1754735610304.zip
    ...
    \[2025-08-09T19:12:01.497\] \[INFO\] default - all 6 package(s) are successfully published
    \[2025-08-09T19:12:01.497\] \[WARN\] default - You are using "filedb" to store data. If you have already started a repository service, please run \`ohpm-repo restart\` to restart the service.
    
    After all packages are successfully published, go to the ohpm-repo website and check whether the number of packages and package details are correct.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/XITUjxOOSRq6D-HRyVOMCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BC152B5C246B488762BAB8CD9F30FAA2783D4A6F8F98EB37ABCC5CEF6A83BDF)
    
    1\. You can append **\--force** to the **batch\_publish** command. If the organization of a package does not exist in ohpm-repo during batch upload, the organization will be automatically created, with any administrator in ohpm-repo selected as its owner.
    
    2\. During batch upload, if the .zip file contains only one repository directory, you can append **\--target-repo _<string>_** to the **batch\_publish** command to upload all packages to the target ohpm-repo repository.
    
4.  Import the package permission data.
    
    Since ohpm-repo 5.4.0, the package permission data can be imported using the [import\_pkgPermission](../../related-commands/data-migration-commands/ohpm-repo-import-pkgpermission/document.md) command. [Three import modes](../../related-commands/data-migration-commands/ohpm-repo-import-pkgpermission/document.md#section8679814134119) are available during the import process. Select an appropriate mode based on the processing rules of each.
    
    PS D:\\> ohpm-repo import\_pkgPermission D:\\packagePermission\_1758008466123.json --mode override
    ...
    \[2025-09-17T14:44:38.451\] \[INFO\] default - > start importing package permissions to the "ohpm" repository.
    \[2025-09-17T14:44:38.459\] \[INFO\] default - import package permissions completed.
