# ohpm-repo pack

Packages the files in the ohpm-repo deployment directory.

#### Prerequisites

The [start](../ohpm-repo-start/document.md) or [restart](../ohpm-repo-restart/document.md) command has been successfully executed, and the ohpm-repo service has been successfully started.

#### Command Format

ohpm-repo pack <deploy\_root>

#### Description

Packages the **conf**, **db**, and **meta** directories in the ohpm-repo deployment directory [deploy\_root](../../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_%E5%85%B3%E4%BA%8E-deploy_root).

Notes:

-   If MySQL is used for the data storage module **db**, running this command will package the **conf** and **meta** directory contents.
-   If FileDB is used for the data storage module **db**, running this command will package the **conf**, **db**, and **meta** directory contents. During the command execution, the ohpm-repo service is set to the read-only mode. After the packaging is complete, the ohpm-repo service is reset to the read/write mode.
-   You can run the **ohpm-repo restore** command to automatically decompress the package to the **<_deploy\_root_\>** directory.

#### Parameters

## <deploy\_root>

-   Type: string
-   Mandatory parameter

You must append the **_<deploy\_root>_** parameter to the **pack** command to specify the [ohpm-repo deployment directory](../../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_%E5%85%B3%E4%BA%8E-deploy_root) to be packaged.

#### Example

Run the following command:

ohpm-repo pack D:\\ohpm-repo

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/kXATLJTHQwibs0IzRUqG2w/en-us_image_0000002532748669.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9429E27B30E160F8B5BF66BAB62B4774A246D75026A82BC990AA192A90989931 "Click to enlarge")
