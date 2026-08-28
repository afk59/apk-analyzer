# What should I do if "error: failed to start ability" is displayed during HAP installation?

**Symptom**

The error message "error: failed to start ability error: ability visible false deny request" is displayed during HAP installation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/BCOZ3p4iTNWeTn3tvG8nFA/en-us_image_0000002229758621.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56C349025A67066FC6C76DA71BD1C7A7F5C53B975415DA11E66A1A418B633EF1)

**Solution**

-   For project developed using the stage model, open the **module.json5** file and set **exported** under **abilities** to **true**.
-   For project developed using the FA model, open the **config.json** file and set **visible** under **abilities** to **true**.
