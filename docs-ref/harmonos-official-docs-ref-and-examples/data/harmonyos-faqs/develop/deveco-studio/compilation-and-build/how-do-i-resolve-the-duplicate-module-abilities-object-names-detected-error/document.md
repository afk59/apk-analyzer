# How do I resolve the "Duplicate 'Module-Abilities' object names detected." error?

**Symptom**

The "Duplicate 'Module-Abilities' object names detected." error is reported during compilation.

**Possible Causes**

There are duplicate names among the ability objects in the **abilities** array in the **module.json5** file of the dependent HAR module.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/qAjEyYVdSnmCbeC9oGRTBg/en-us_image_0000002194158504.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D32230C654BABECEE6CF7062B7FB47FEAD5F7174C30B1F2320196071B1B817F5)

**Solution**

Open the **module.json5** file of the dependent HAR module and make sure each ability object in the **abilities** array has a unique name.
