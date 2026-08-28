# How do I resolve the "CMake task execution failed" error?

**Symptom**

During CMake task execution, the error message "CMake task execution failed" appears.

**Possible Causes**

The **.cxx** directory need to be manually removed, and the **\--version** parameter need to be configured under the **arguments** field in the **build-profile.json5** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/84baiLSsSdmvn6HCS-VUvQ/en-us_image_0000002229604133.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F95230A798611F48AC8F397013CCBB4059ACD431E3E691A3F4C2CA19B484A22A)

**Solution**

Delete the **\--version** parameter from the **arguments** field.
