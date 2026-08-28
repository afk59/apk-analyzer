# What should I do if the memory of the Memory lane is different from that of the Native Allocation lane when recording the Allocation template?

**Symptom**

The memory of the Memory lane is different from that of the Native Allocation lane when recording the Allocation template.

**Possible Causes**

The Memory lane displays the actual physical memory usage (Proportional Set Size, PSS) of the selected application, while the Native Allocation lane shows the virtual memory dynamically requested by the application from the operating system during runtime, which does not represent the actual physical memory usage.

**Solution**

Before starting recording, click on the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/zHw_6vufQ2C-GuB5C5163Q/en-us_image_0000002513253146.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=968460CA8C50B98AAEF747374049520C6DB953DB193BBAFD176C5F19EF355E48) button on the toolbar to set Native Allocation Filter Size to **0** or the minimum value, so that more or even all virtual memory allocation events can be collected. In this way, the data changes in the Native Allocation lane are similar to those in the Memory lane.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/fXbcFM2AS9KQuwkjxVFm2A/en-us_image_0000002544733119.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=583ADE2078C1598176F1497040BE8FC4FFCB07B859293A575DF78EA49E38E7F3 "Click to enlarge")
