# What should I do if historical data fails to be imported?

**Symptom**

When the Profiler **.insight** file exported from DevEco Studio of another version is used, any of the following exceptions occurs:

-   Import failed.
-   The lane is not displayed after import.
-   No data is found after import.

**Solution**

The version of DevEco Studio used to import the file must be the same as that used to export the file.

You can determine the DevEco Studio version based on the **devEcoStudioBuildVersion** field in **manifest.json** in the **.insight** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/W3-sog4YQZG4B8oRfiB6_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1A6893812667C891CDDA0A3B167CD37935A30F6D4D498AD175DB901FB1EC0B8)

The **.insight** file can be opened using common decompression software.
