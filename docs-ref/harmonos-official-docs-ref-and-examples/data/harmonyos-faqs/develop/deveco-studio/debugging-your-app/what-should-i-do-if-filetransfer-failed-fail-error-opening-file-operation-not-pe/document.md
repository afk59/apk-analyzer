# What should I do if "FileTransfer Failed: \[Fail\]Error opening file: operation not permitted" is displayed during HAP installation on DevEco Studio?

**Symptom**

The error message "FileTransfer Failed: \[Fail\]Error opening file: operation not permitted" is displayed during HAP installation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/0qh0V77mQUKeyvV-l0vP0g/en-us_image_0000002390254777.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7628F3A0AEF54D24237E3ABB51BDB203FC2F72204D5B405158815B8FFCDA7927)

**Solution**

The issue occurs because you do not have the permission to access the path where the HAP installation package is stored. Move the project out of drive C and install it again.
