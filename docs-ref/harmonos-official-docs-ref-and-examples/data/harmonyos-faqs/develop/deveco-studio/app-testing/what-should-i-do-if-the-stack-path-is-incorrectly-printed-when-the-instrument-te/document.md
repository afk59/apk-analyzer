# What should I do if the stack path is incorrectly printed when the instrument test is executed using a command?

**Symptom**

In DevEco Studio 5.0.3.400, when an instrument test is performed using the command, the file path and location in the stack information is incorrect ("|" instead of "/"). The problem persists after the DevEco Studio version is upgraded to 5.0.3.401 or later.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/afKncS4JRKak7zfUNhrHkg/en-us_image_0000002194158620.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4677D3CC6AC7E568D4409C91F9A77476BC9129BE64B8EF2673FCDEF789F55095 "Click to enlarge")

**Possible Causes**

The **.test** and the **build** folders generated in DevEco Studio 5.0.3.400 are not deleted.

**Solution**

Delete the **.test** and **build** folders and execute the test case again.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/rT8BA_C_Tvmf7ieRPo0F2A/en-us_image_0000002194318232.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5326A6306343E2FC2B82847FF72EF4B04AE1776DBBC436748F88A0F148285BEC "Click to enlarge")
