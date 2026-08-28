# What should I do if "error: unlock screen failed in developer mode" is displayed during HAP installation?

**Symptom**

The error message "error: failed to start ability. error: unlock screen failed in developer mode" is displayed during HAP installation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/mGmwAAK_RhSxvoossWQ5Eg/en-us_image_0000002194317996.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=001C626C99C8A320BC46DD6549F35BE467C5D19072BA6CAE6BADE954DD30497D "Click to enlarge")

**Solution**

This issue occurs when the device is locked and has a lock screen password set. To resolve this, use either of the following methods:

-   Method 1: Choose **Settings** > **Display & brightness** > **SCREEN** > **Sleep** to extend the automatic sleep time.
-   Method 2: During application development, avoid setting a lock screen password. This way, the device will automatically wake up and launch the application when it starts.
