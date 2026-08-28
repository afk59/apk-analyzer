# ohpm-repo install

Installs the ohpm-repo service.

#### Command Format

ohpm-repo install \[options\]

#### Description

Before starting the service, make preparations, including checking the validity of the ohpm-repo configuration file and initializing the database.

#### Options

## config

-   Default value: **_<binary\_root>_/conf/config.yaml**
    
    **<binary\_root>**: root directory where the ohpm-repo tool package is decompressed.
    
-   Type: string
    

You can specify the configuration file path by appending the **\--config <string>** parameter to the **install** command. The relative path is supported. The current working path of the command line is used as the root directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/GLo0xG-XRSetuFqcgjmcpg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CEAECF89C416063D98C3B758E87C98885FCB460A61C692F28A11AFB7CDF4AE6)

After the **install** command is successfully executed, a runtime configuration file **config.yaml** is generated in **<_deploy\_root_\>/conf** as the configuration file for subsequent commands. **<_deploy\_root_\>** indicates the [ohpm-repo deployment directory](../../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_%E5%85%B3%E4%BA%8E-deploy_root).

## skip-db

-   Default value: **false**
-   Type: Boolean
-   Alias: s

Append **\-s** or **\--skip-db** to the **install** command to specify whether to skip the initialization of data tables in the MySQL database. By default, the **schema.sql** file in the directory where the ohpm-repo package is decompressed is read to initialize tables in the MySQL database.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/EuSwQpEeQymEobpmsQBbNw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DE6A8922DB2DE2DEE86B85F8A8B56C9AC1D94C45A3983014B6A2D0B223B0133)

1\. In the ohpm-repo configuration file **config.yaml**, this parameter takes effect only when **db.type** is set to **mysql**.

2\. Since ohpm-repo 5.2.0, the parameter **\-sd** has been marked as deprecated. Replace **\-sd** with **\-s** in the configuration. **\-sd** will be removed in later versions.

## diagnosis-and-repair

-   Default value: **false**
-   Type: Boolean
-   Alias: dr

Append **\--dr** or **\--diagnosis-and-repair** to the **ohpm-repo install** command to diagnose and repair the package permission table. By default, the package permission table is not diagnosed or repaired if this configuration is not added.

#### Example

Run the following command:

ohpm-repo install  --config D:\\config.yaml

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/IdZR2sS-RM6qrXDDgW0chQ/en-us_image_0000002532748693.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5EEA0123638395B0364E1E2127DAD86939D8614D36A5167827392CB1769E34D "Click to enlarge")

#### Note

After the installation is successful, you must reload environment variables based on the displayed information. The reload method varies with the operating system — Windows or Linux/macOS.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/lu77kAeFRKagiW6CVfGp6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2AE078BB1F57A17280D04DCC2669679DD179DD9118756E59E5FDCFCC6C4DEFF)

-   Windows: Close the current window and open a new window.
-   Linux or macOS: Run the _**source ~/.bashrc**_ or **_. ~/.bashrc_** command on the CLI to reload environment variables.
