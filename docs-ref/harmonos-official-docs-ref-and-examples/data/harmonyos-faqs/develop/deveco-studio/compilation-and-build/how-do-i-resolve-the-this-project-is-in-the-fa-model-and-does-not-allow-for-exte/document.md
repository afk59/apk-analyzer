# How do I resolve the "This project is in the FA model and does not allow for external dependencies." error?

**Symptom**

The "This project is in the FA model and does not allow for external dependencies." error is reported during compilation.

**Possible Causes**

In the **build-profile.json5** file of the project developed in the FA model, the value of the **srcPath** field contains a reference to an external project module.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/wK1MjJQJTQGInyfWzhYmWQ/en-us_image_0000002194318412.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37572AEB8FCDB5FEF60FDE71D0CFAC35A71F565455E53A53202915C3B9E64B4E)

**Solution**

In the **build-profile.json5** file located in the project root directory, identify and remove any references to external project modules from the **srcPath** field.
