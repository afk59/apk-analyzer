# ohpm-repo start

Starts the ohpm-repo service.

#### Prerequisites

The [install command](../ohpm-repo-install/document.md) has been successfully executed, and environment variables have been updated as required.

#### Command Format

ohpm-repo start 

#### Description

Starts the ohpm-repo service and creates an ohpm-repo instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/s8VduhFeSK6DW25HIGW-VA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F319FE2F1333F203E883156657947C398D7637547F1D6CA69154FFA3E20255E)

During startup, **pid** of the ohpm-repo service is stored in the **<_deploy\_root_\>/runtime/.pid** file, where **<_deploy\_root_\>** indicates the [ohpm-repo deployment directory](../../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_%E5%85%B3%E4%BA%8E-deploy_root).

#### Example

Run the following command:

ohpm-repo start

Below is an output example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/ozUlgVi4TLGq2CivXdXHpQ/en-us_image_0000002500908840.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4413BE81E1A13A2915784F437C9262DB6A42BFCEBB9A8E46AAF937DE5BD1CF5 "Click to enlarge")
