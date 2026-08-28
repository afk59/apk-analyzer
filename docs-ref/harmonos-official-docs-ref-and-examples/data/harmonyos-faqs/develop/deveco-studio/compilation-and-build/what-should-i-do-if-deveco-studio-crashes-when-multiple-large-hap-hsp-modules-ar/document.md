# What should I do if DevEco Studio crashes when multiple large HAP/HSP modules are compiled concurrently?

**Symptom**

When an application contains multiple HAP/HSP modules and the code volume of each module is at the level of 1 million lines, DevEco Studio crashes unexpectedly after directly clicking the build option (click **Build** > **Build Hap(s)/APP(s)**) in the tool.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/Co7if1EOR0OIebxXI2trGw/en-us_image_0000002515675178.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48CA989FED8A3E671CD8AD64809423386DFB81FA4DC0252151EC3AB5AF7949B8)

**Possible Causes**

When the code volume of a single module exceeds 1 million lines, compiling that single module consumes more than 5 GB of memory. Parallel compilation of 4 or more modules will result in memory usage reaching 20 GB, leading to insufficient system memory.

**Solution**

Change parallel compilation to serial compilation for execution. In DevEco Studio, select each module one by one and then click to compile it (select the module on the left side, click **Build**, and then click the first button: **Make Module 'xxx'**).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/p4INP1vrQgOr7TY3FLNX_w/en-us_image_0000002515835104.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F235C77A22C4B28F7B0AB2169AE42F2783829B62B33ABA1797D056A14B1AC9F9)
