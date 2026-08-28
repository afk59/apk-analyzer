# What should I do if there is no data in the OpenGL ES sub-lane within the Graphic Memory lane when recording the Allocation template on a PC device?

**Symptom**

When using a PC device, the OpenGL ES sub-lane in the Graphic Memory lane shows no data when recording the Allocation template in FP back-stack mode.

**Possible Causes**

The GPU underlying library does not support the FP back-stack mode.

**Solution**

Before starting recording, click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/aJxwDWn4QUit-50BGISJ6w/en-us_image_0000002538356035.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94C119F5F2B065FAB712B335B85110881C439CF172D6D3CE2DD9FF7F1EAA344B "Click to enlarge") button in the tool's control bar and set the memory allocation stack backtrace mode to DWARF. When collecting data in DWARF backtrace mode, the performance overhead is relatively high. Therefore, it is recommended not to record the Native Allocation lane at the same time when recording the Graphic Memory lane.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/sogtEqP6TU-_i9U6zNZyFQ/en-us_image_0000002506636162.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBA088793080E20ABE825024897532DAABF067D98273BCBF431727ADB4A99F5C "Click to enlarge")
