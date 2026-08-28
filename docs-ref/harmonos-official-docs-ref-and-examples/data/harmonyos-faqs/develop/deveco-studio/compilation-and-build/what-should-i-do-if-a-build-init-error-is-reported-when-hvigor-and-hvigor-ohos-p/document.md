# What should I do if a Build Init error is reported when Hvigor and hvigor-ohos-plugin versions are changed during synchronization?

**Symptom**

After configuring the Hvigor and hvigor-ohos-plugin versions, click **Sync**. If the version number is changed again, the download will be repeated, causing a version conflict. As a result, a Build init error is reported and logs are refreshed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/i5Q2Z0-BT4iHCxWuUIMGHA/en-us_image_0000002194158832.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6ACB83BF021A2C8CCC68052233831D9ED3AF195E3658A6FCA0D8DFC55C0108E7)

**Solution**

This problem occurs because the Hvigor version is changed when **build init** is executed to download Hvigor. When **hvigor.js** is executed, the dependency changes. As a result, the new version is downloaded for the second time, causing an incompatibility problem. You are advised not to change the Hvigor version when executing **Sync** and downloading Hvigor.

Choose **File** > **Sync and Refresh Project** to synchronize again.
