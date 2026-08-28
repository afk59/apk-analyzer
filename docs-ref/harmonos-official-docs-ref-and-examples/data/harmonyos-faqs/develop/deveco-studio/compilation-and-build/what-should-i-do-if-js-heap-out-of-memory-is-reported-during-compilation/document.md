# What should I do if "JS heap out of memory" is reported during compilation?

**Symptom**

"JS heap out of memory" is reported during compilation and build.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/CoA1knoETRS8_-r__DWkTQ/en-us_image_0000002194158628.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F2FBF5A82F7FD88DB51F377AFDF60B095FE800E1A405D9A818C63FD87BF6575)

**Solution**

This error occurs due to insufficiency memory when Hvigor is running. If Hvigor 3.1.0 or later is used, you can perform the following operations to change the maximum runtime memory size of Hvigor:

Select **Enable the Daemon for tasks**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/abYdt0-iT7OTNOtSR0nmSw/en-us_image_0000002194318244.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADEDEA50FF015A3D6E47ED44FD3029DC19605DD43D7669CC78AEA7977E84E3DD)

Increase the value of **maxOldSpaceSize** in **hvigor-config.json5** according to the project size, for example, set it to **8192**.
