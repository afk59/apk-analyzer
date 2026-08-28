# What should I do if no data is displayed on the Load ETS Files and TOP Redundant tabs of the Details page of the Launch lane in DevEco Profiler?

**Symptom**

In the **Launch** lane of DevEco Profiler, when the monitoring time for ETS file is set to **20000**, no data is displayed on the **Load ETS Files** and **TOP Redundant** tabs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/qsJR7gEFRkaAVkhCVn2BeA/en-us_image_0000002314311052.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0553F028FC7C04FE656DAC0F133B69CD76362E4B550707AD84B6508CE00B415 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/ZrHuRrCrRYWPnbra57xm0A/en-us_image_0000002314151220.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E3A6C0FC938F7BEE55BC49775660C7DD0A92337273C67EC85BC2667AC90C4EB "Click to enlarge")

**Possible Causes**

If the monitoring time for the ETS file is set to **20000**, the ETS redundant logging file can be generated 20000 ms after the application is started.

**Solution**

After the monitoring time for the ETS file is set to **20000**, the recording duration must be longer than the configured duration.
