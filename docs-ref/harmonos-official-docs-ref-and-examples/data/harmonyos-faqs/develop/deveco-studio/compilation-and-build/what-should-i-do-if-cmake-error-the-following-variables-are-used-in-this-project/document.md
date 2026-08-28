# What should I do if "CMake Error: The following variables are used in this project, but they are set to NOTFOUND" is reported during compilation?

**Symptom**

An error is reported when find\_path is used in a native project, because the target file is not found in the path specified by **CMAKE\_SYSROOT**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/CVilh-LeQCSheUje4-tiMg/en-us_image_0000002229603961.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5A2DDA89E6E13A293181885FDF68FE894FDC80D1CC2989AA1DB6DD364D94C51 "Click to enlarge")

**Solution**

The **ohos.toolchain.cmake** file of the OpenHarmony SDK restricts the search path to **CMAKE\_SYSROOT**.

If you need to add a search path, use the **list** API to add a custom path in **CMakeList.txt**. For example, add **D:/demo** to the search path.

list(APPEND CMAKE\_FIND\_ROOT\_PATH\_MODE\_INCLUDE "D:demo")

After the path is added, you can use **find\_path** to search files in the **D:/demo** directory.
