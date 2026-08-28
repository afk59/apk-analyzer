# How do I resolve the "The path XX is not writable. Please choose a new location" error?

**Symptom**

When DevEco Studio is opened from a .dmg file on macOS, any attempt to build a project results in the error message "The path XX is not writable. Please choose a new location."

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/7UWM5dEsRBmylumTN4bc2Q/en-us_image_0000002229604193.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=091371F6CD75267B3AEFDBF01A2D1D88B56168B5423FECA063B34D5191A7EE30)

**Possible Causes**

Opening DevEco Studio on macOS from the .dmg file launches it in read-only mode, and the files built into DevEco Studio do not have write permissions.

**Solution**

Drag **DevEco-Studio.app** to **Applications** and install DevEco Studio by following the onscreen instructions.
