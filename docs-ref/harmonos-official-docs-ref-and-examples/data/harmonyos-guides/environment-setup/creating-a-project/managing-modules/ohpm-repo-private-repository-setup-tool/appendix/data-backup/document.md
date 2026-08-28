# Data Backup

Before data migration or version upgrade, you must back up data to prevent loss of important data and rollback failure. The following data needs to be backed up: data in the ohpm-repo deployment root directory **<_deploy\_root_\>**, metadata in **db**, and third-party package data in **store**.

#### Backup of the deploy\_root Directory

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/byqfW8kqSqekgfz4-2CmlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01B54128612DF70CFEC05DD8A723B311291082E4A8CDFA0AFF2CA004B3777740)

**<_deploy\_root_\>**: root directory for deploying ohpm-repo. The default value is as follows:

Windows: **~/AppData/Roaming/Huawei/ohpm-repo**

Others: **~/ohpm-repo**

In versions earlier than 1.1.0, **<_deploy\_root_\>** cannot be configured for ohpm-repo. The default values are used. If **<_deploy\_root_\>** is configured for your ohpm-repo, find the corresponding directory and use a common compression tool to compress and back up the directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/-eKnVvA3QTqeortL4WaH9g/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0423562750E3CF8E6C0E2AF9BC7EC73199C4A9431BE2EC309733EA66D588FA81)

If the storage paths of **db**, **storage**, **logs**, and **uplink** in the configuration file are configurable and are not in the root directory **<_deploy\_root_\>** where ohpm-repo is deployed, locate the corresponding directory for data backup.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/WWXcB6vaQgGrL0e7owwJTg/en-us_image_0000002532668729.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E1D2D381A1BFFAA09FAB6A8AA69F303B6CAC7ACE427531F3BF5E6C7B9AA37CD "Click to enlarge")

#### Backup of <Package Storage Directory> and MySQL Database

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/Naf40bvkQg2MfK82YV8KoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B3B3863575279F2E415CC37AF529509EF4AD17E79C4FC7E4F69A32E983AB2F7)

If you use local storage (**db** indicates the FileDB local storage and **store** indicates the FS local storage in the configuration file), skip this step because **db** and **store** have been backed up during **<_deploy\_root_\>** backup.

-   If **type** under **db** is configured as **mysql**, back up the database structure and data based on the configured database name.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/aBG9D3y3RpelsOL3rY9Pdg/en-us_image_0000002500908824.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3174B7FF027D5106874B84076A60BFD7B132C45D0EBE2EEF3389AED33CC4457D "Click to enlarge")
    

-   If the **store** configuration option uses the SFTP storage or customized storage plugin, perform backup based on the configured storage directory. (The following figure uses SFTP storage as an example.)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/Qt3lTiCiTcav1_iXb4Qbrg/en-us_image_0000002532748685.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E454AECF2A9B24AF3060D6CC117239066487D50CDD6939A24F1E2B4AE9F49059 "Click to enlarge")
