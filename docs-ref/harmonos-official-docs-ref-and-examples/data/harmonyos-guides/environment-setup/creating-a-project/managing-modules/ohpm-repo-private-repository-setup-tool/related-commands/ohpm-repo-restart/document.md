# ohpm-repo restart

Restarts the ohpm-repo service.

#### Prerequisites

The [install command](../ohpm-repo-install/document.md) has been successfully executed, and environment variables have been updated as required.

#### Command Format

ohpm-repo restart 

#### Description

Stops the current ohpm-repo service and restarts a new ohpm-repo service.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/OB2fE2WMTOiEn6bnoSni9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4221E5125B63122B9F299416DD5348A91F6AB97E5E78562EBC83072808DCAEF1)

During startup, **pid** of the ohpm-repo service is stored in the **<_deploy\_root_\>/runtime/.pid** file, where **<_deploy\_root_\>** indicates the [ohpm-repo deployment directory](../../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_%E5%85%B3%E4%BA%8E-deploy_root).

#### Example

Run the following command:

ohpm-repo restart

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/HgtdEjUBT9qmwr_xhBYGyQ/en-us_image_0000002532668823.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5649D79A96348EC32240D1DDBCE298A51C4450163C1C0FBE7C356F46A1BEED16 "Click to enlarge")
