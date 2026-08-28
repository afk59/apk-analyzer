# How do I resolve the "The required attribute module-srcPath is missing" error?

**Symptom**

The "The required attribute module-srcPath is missing" error is reported during compilation.

**Possible Causes**

The **build-profile.json5** file does not contain the relative path of the module, that is, the **module-srcPath** field is missing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/mr_qY90sSFupjiateY_ORg/en-us_image_0000002229758669.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5027A06D9EBEFF986FC47532D3B9E54E3B8ADF6FF68CE96F35E70347C38A7B25)

**Solution**

Open the **build-profile.json5** file in the root directory of the project and ensure that the **srcPath** field exists under **module** and is not empty.
