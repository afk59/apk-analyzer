# How do I resolve the "Failed to obtain the module type." error?

**Symptom**

The "Failed to obtain the module type." error is reported during compilation.

**Possible Causes**

In projects developed using the FA model, the **module/distro/moduleType** field is missing or incorrectly configured in the **config.json** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/VzrdX6IET2qAlpE5cJlkgQ/en-us_image_0000002229604177.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20C9ABB74CFB6E5743F8B136AABF8D7BCA25C2F853F0B35BD66112431580EFB8)

**Solution**

For projects developed using the FA model, make sure the **config.json** file contains a correctly configured **module/distro/moduleType** field.
