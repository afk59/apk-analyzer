# How do I configure DevEco Studio to ignore the assert signal caught by raise?

Open the **Run/Debug Configurations** window, choose **Edit Configurations** > **Debugger** > **LLDB Post Attach Commands**, and add the following configuration: **process handle -p false -s false -n false signal**, where **signal** is the signal sent by **assert**. The following figure shows the procedure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/8hlBQLjMT_uP6j2uCjq1CA/en-us_image_0000002194158524.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=333378F4015D9349A6F86F3A7BEB5D31F562314EFE941799F7C24EAAD8070154)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/mlNdo8WzSGKNpMebpGWNUQ/en-us_image_0000002229603925.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BABFA81773A5E4F67EADB809F0130E2DE1C0D30A75606A3C416E944409E99AC "Click to enlarge")
