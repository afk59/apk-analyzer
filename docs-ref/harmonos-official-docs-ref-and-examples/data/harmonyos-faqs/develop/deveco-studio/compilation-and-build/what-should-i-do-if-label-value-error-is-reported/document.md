# What should I do if "LABEL\_VALUE\_ERROR" is reported?

**Symptom**

**LABEL\_VALUE\_ERROR** is reported during project synchronization, compilation, or build.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/nUnfOrJtQEKRH4GVQNxDmA/en-us_image_0000002229758717.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9F7F0DBE8C393813D184471EF810DFFC0CC6E4C3179FA6A1274B1856401DF42)

**Solution**

The resource reference rules of the **config.json** file have changed. Change the value of the **label** field to the resource reference mode.

1.  Choose **resources** > **base** > **element** and add the corresponding string to the **string.json** file.
2.  Reference the string resource again in the **config.json** file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/dTF1D_MdSMOVPI7XxdaQog/en-us_image_0000002194158844.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C701E2CEFAD9815D7AFF73C553196577E5D1E371D3C46EF05C34911DB2E8258)
