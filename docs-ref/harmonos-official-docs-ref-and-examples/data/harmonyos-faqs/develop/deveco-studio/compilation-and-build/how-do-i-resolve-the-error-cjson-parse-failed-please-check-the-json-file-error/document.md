# How do I resolve the "Error: cJSON\_Parse failed, please check the JSON file." error?

**Symptom**

The error message "Error: cJSON\_Parse failed, please check the JSON file." is displayed during compilation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/v5CnfpicQ-20lRYQRiZcsw/en-us_image_0000002194158800.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1150F6CA9CE33E39EEBCF82074BC48EFA9EEAFBB9A45FC935285E0E942A4712 "Click to enlarge")

**Possible Causes**

The **module.json** file format is invalid.

**Common Scenarios**

1\. The .json file has an extra comma (,) at the end.

2\. The root element is not enclosed in curly braces ({}).

**Solution**

Verify the format of the JSON file indicated by the error.
