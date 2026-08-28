# What should I do if the hdc cannot access the device after installing the VPN software astrill?

**Symptom**

The hdc cannot access the device. The **hdc list targets -v** command returns the "unknown" status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/UWVAumfcQWq6M72xLkUTZA/en-us_image_0000002474863621.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062535Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC3946CDB2694036ECCE994118EB7510C92A804D03BEBBB02B6459F874754CE7)

Viewing the **hdc.log**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/ipj9T1r2TJKIZz6RoGqDeg/en-us_image_0000002474943789.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062535Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B1D487BF4E03E05EC225EB9E715C9D4042AD9FD2905E1B4C8E9EA77AF69D8CC)

**Possible Causes**

There are system compatibility issues. This problem occurs when the VPN tool astrill is installed on Windows 10.

**Solution**

-   For the current hdc version, you are advised to uninstall the VPN software, rather than simply closing it.
-   Upgrade to the latest version by referring to the [hdc Version Mappings](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#hdc-version-mappings) and try again.
