# How do I resolve the "Duplicate 'routerMap' object names detected." error?

**Symptom**

The "Duplicate 'routerMap' object names detected." error is reported during compilation.

**Possible Causes**

The **router\_map.json** file of the current module contains **routerMap** configurations with duplicate names, either within the current module or between the current module and its dependent modules.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/EofHPpQVSrWz3u58x-lLBQ/en-us_image_0000002229603813.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C97666FE40744A92D90745A6C2F0FF83B5FCCA1E02763369CE3E1B875F26F48)

**Solution**

Make sure all **routerMap** configurations in the **router\_map.json** file have unique names.
