# What should I do if the Profiler window fails to load?

**Symptom**

The Profiler window displays the "There is already a Profiler running." message.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/shif8ZcHT5CVUXlStcUWjw/en-us_image_0000002273437384.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C156842ACA1BF4375A3086566E157E70B97FC2CCBED4F23BC26F97DA498FEE34 "Click to enlarge")

**Possible Causes**

Profiler operates in singleton mode. Only one Profiler instance can run across multiple DevEco Studio sessions.

**Solution**

-   Close the current DevEco Studio session and use Profiler in the DevEco Studio session where the Profiler window loads correctly.
    
-   Close all other DevEco Studio sessions. Click the "There is already a Profiler running." message in the active DevEco Studio session, and wait for the Profiler window to refresh.
