# How do I resolve the "The permission under requestPermissions must be a value that is predefined within the SDK or a custom one that you have included under definePermissions." error?

**Symptom**

The "The permission under requestPermissions must be a value that is predefined within the SDK or a custom one that you have included under definePermissions." error is reported during compilation.

**Possible Causes**

The permission name under **requestPermissions** in the **module.json5** file is invalid or the permission is not supported by the current version.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/-k2eIkm8T16Pj0BQyGlwvQ/en-us_image_0000002229604097.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CDD763AAA65C553E4F12560B4630AA8150C079805DD37288DBBB70CD90C270A)

**Solution**

Update the value of the **name** field under **requestPermissions** to a valid permission name, either predefined in the SDK or custom-defined under **definePermissions**. If the permission is not supported by the current version, you are advised to upgrade the API version.
