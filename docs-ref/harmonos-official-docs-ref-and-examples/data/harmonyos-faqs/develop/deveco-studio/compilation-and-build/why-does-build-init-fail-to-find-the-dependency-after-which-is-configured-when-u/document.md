# Why does Build Init fail to find the dependency after which is configured when updating Hvigor?

**Symptom**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/zG4iJ6KARreLYjHlY58RaQ/en-us_image_0000002194158852.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A3F51AD7CB8C857877FCE95B7E93CC42F7164E95D5A98ED7E752FB8B9E207C0)

**Solution**

This issue occurs because the project uses Hvigor 3.3.0 or a later version, but the **hvigor-wrapper.js** version is too old and incompatible with Hvigor. The incompatibility scenarios are as follows:

-   Scenario 1: For DevEco Studio earlier than 4.0 Canary2, only Hvigor is downloaded during synchronization while the dependencies listed under **dependencies** (hvigor-ohos-plugin) are not downloaded. If you want to update Hvigor without updating DevEco Studio, only Hvigor rather than hvigor-ohos-plugin can be downloaded. In this case, update DevEco Studio to DevEco Studio NEXT Developer Preview1 or a later version.
-   Scenario 2: For projects created using DevEco Studio earlier than 4.0 Beta1, you need to update Hvigor. In this case, use DevEco Studio NEXT Developer Preview1 or a later version to open a historical project, modify Hvigor and the plugin version numbers in **hvigor-config.json5**, and click **Sync**. During the sync, the system will remind you to update Hvigor and its plugin. After you click the update button, Hvigor and its plugin will be automatically downloaded.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/NmO-gICjTwCL0HapJ0tRGw/en-us_image_0000002229758729.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A80A9D4BB57DA9174FBCF046366257F30A03D17A85F0AA653F563CA6DDE7BE2B)
