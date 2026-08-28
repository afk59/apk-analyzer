# How do I resolve the "The reason attribute are mandatory for user\_grant permissions." error?

**Symptom**

The "The reason attribute are mandatory for user\_grant permissions." error is reported during compilation.

**Possible Causes**

The **reason** field is not configured as expected for permissions of the user\_grant type in the **module.json5** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/IXvdLm4XSGamJGvJFNzrIg/en-us_image_0000002229758313.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E014B554D5A96296F2BEB0B58E20609019C231361D76D0E300DD95AB9654ADA3)

**Solution**

For HAP modules, make sure both the **reason** and **usedScene** fields are configured under **requestPermissions** in the **module.json5** file.

For HAR and HSP modules, make sure the **reason** field is configured under **requestPermissions** in the **module.json5** file.
