# How do I resolve the "The reason and usedScene attributes are mandatory for user\_grant permissions." error?

**Symptom**

The "The reason and usedScene attributes are mandatory for user\_grant permissions." error is reported during compilation.

**Possible Causes**

The **reason** and **usedScene** field is not configured as expected for permissions of the user\_grant type in the **module.json5** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/XzMYZAudQbSSxQCipk4_sg/en-us_image_0000002194158708.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B92D0AC80FE60F65F561BD770D169E29D3AA7271C0421D0EA2E485B5D5377A56)

**Solution**

For HAP modules, make sure both the **reason** and **usedScene** fields are configured under **requestPermissions** in the **module.json5** file.

For HAR and HSP modules, make sure the **reason** field is configured under **requestPermissions** in the **module.json5** file.
